from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.api_change import ApiChange
from app.models.api_source import ApiSource
from app.models.api_version import ApiVersion
from app.models.dependency import Dependency
from app.models.fix import Fix
from app.models.impact_report import ImpactReport
from app.models.test_run import TestRun
from app.schemas.source import SourceCreate, SourceResponse, SpecPathUpdate
from app.schemas.dependency import DependencyCreate
from app.services.scanner import scan_source
from app.services.fix_generator import generate_fix
from app.services.test_runner import run_tests

router = APIRouter(prefix="/api", tags=["NovaGrid"])

@router.post("/sources", response_model=SourceResponse)
def create_source(payload: SourceCreate, db: Session = Depends(get_db)):
    source = ApiSource(**payload.model_dump()); db.add(source); db.commit(); db.refresh(source); return source

@router.get("/sources", response_model=list[SourceResponse])
def list_sources(db: Session = Depends(get_db)):
    return db.query(ApiSource).order_by(ApiSource.id).all()

@router.get("/sources/{source_id}", response_model=SourceResponse)
def get_source(source_id: int, db: Session = Depends(get_db)):
    source = db.get(ApiSource, source_id)
    if not source: raise HTTPException(404, "API source not found")
    return source

@router.put("/sources/{source_id}/spec-path")
def update_spec_path(source_id: int, payload: SpecPathUpdate, db: Session = Depends(get_db)):
    source = db.get(ApiSource, source_id)
    if not source: raise HTTPException(404, "API source not found")
    source.spec_path = payload.spec_path; source.spec_url = None; db.commit()
    return {"source_id":source_id,"spec_path":source.spec_path}

@router.post("/sources/{source_id}/scan")
def scan(source_id: int, db: Session = Depends(get_db)):
    source = db.get(ApiSource, source_id)
    if not source: raise HTTPException(404, "API source not found")
    try: return scan_source(db, source)
    except (FileNotFoundError, ValueError) as exc: raise HTTPException(400, str(exc)) from exc

@router.get("/sources/{source_id}/versions")
def versions(source_id: int, db: Session = Depends(get_db)):
    return db.query(ApiVersion).filter(ApiVersion.source_id == source_id).order_by(ApiVersion.version_number).all()

@router.post("/dependencies")
def create_dependency(payload: DependencyCreate, db: Session = Depends(get_db)):
    if not db.get(ApiSource, payload.source_id): raise HTTPException(404, "API source not found")
    item = Dependency(**payload.model_dump()); db.add(item); db.commit(); db.refresh(item); return item

@router.get("/sources/{source_id}/dependencies")
def dependencies(source_id: int, db: Session = Depends(get_db)):
    return db.query(Dependency).filter(Dependency.source_id == source_id).order_by(Dependency.id).all()

@router.get("/sources/{source_id}/changes")
def changes(source_id: int, db: Session = Depends(get_db)):
    return db.query(ApiChange).filter(ApiChange.source_id == source_id).order_by(ApiChange.created_at.desc()).all()

@router.get("/changes/{change_id}")
def change_detail(change_id: int, db: Session = Depends(get_db)):
    change = db.get(ApiChange, change_id)
    if not change: raise HTTPException(404, "Change not found")
    return {"change":change,"impacts":db.query(ImpactReport).filter(ImpactReport.change_id==change_id).all(),"fixes":db.query(Fix).filter(Fix.change_id==change_id).all(),"test_runs":db.query(TestRun).filter(TestRun.change_id==change_id).all()}

@router.post("/changes/{change_id}/generate-fixes")
def generate_fixes(change_id: int, db: Session = Depends(get_db)):
    change = db.get(ApiChange, change_id)
    if not change: raise HTTPException(404, "Change not found")
    impacts = db.query(ImpactReport).filter(ImpactReport.change_id == change_id, ImpactReport.file_path != "Unknown").all()
    generated=[]
    for item in change.changes_json:
        if "path" not in item: continue
        for report in impacts:
            dep = db.query(Dependency).filter(Dependency.source_id==change.source_id, Dependency.file_path==report.file_path).first()
            if not dep: continue
            fix=generate_fix(item,dep); db.add(Fix(change_id=change.id,description=fix["description"],patch=fix["patch"],status=fix["status"])); generated.append(fix)
    db.commit(); return {"change_id":change_id,"fixes_generated":len(generated),"fixes":generated}

@router.get("/changes/{change_id}/fixes")
def fixes(change_id: int, db: Session = Depends(get_db)):
    return db.query(Fix).filter(Fix.change_id==change_id).order_by(Fix.id).all()

@router.post("/changes/{change_id}/test")
def test_change(change_id: int, db: Session = Depends(get_db)):
    change=db.get(ApiChange,change_id)
    if not change: raise HTTPException(404,"Change not found")
    source=db.get(ApiSource,change.source_id); cwd=source.repo_path if source and source.repo_path else "."
    result=run_tests(cwd); db.add(TestRun(change_id=change_id,passed=result["passed"],exit_code=result["exit_code"],output=result["output"],duration_seconds=result["duration_seconds"])); db.commit(); return result

@router.get("/changes/{change_id}/test-runs")
def test_runs(change_id:int, db:Session=Depends(get_db)):
    return db.query(TestRun).filter(TestRun.change_id==change_id).order_by(TestRun.id).all()
