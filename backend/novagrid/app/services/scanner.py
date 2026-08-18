from sqlalchemy.orm import Session
from app.models.api_change import ApiChange
from app.models.api_source import ApiSource
from app.models.api_version import ApiVersion
from app.models.impact_report import ImpactReport
from app.services.ai_analyzer import analyze_change
from app.services.diff_engine import compare_specs
from app.services.impact_analyzer import find_impacts
from app.services.spec_loader import calculate_hash, load_spec

def scan_source(db: Session, source: ApiSource) -> dict:
    location = source.spec_path or source.spec_url
    if not location: raise ValueError("No API specification configured")
    spec = load_spec(location)
    spec_hash = calculate_hash(spec)
    latest = db.query(ApiVersion).filter(ApiVersion.source_id == source.id).order_by(ApiVersion.version_number.desc()).first()
    if latest and latest.spec_hash == spec_hash:
        return {"changed":False,"version":latest.version_number,"changes_detected":0,"classification":"UNCHANGED","changes":[]}
    version = ApiVersion(source_id=source.id, version_number=(latest.version_number+1 if latest else 1), spec_hash=spec_hash, spec_json=spec)
    db.add(version); db.flush()
    changes = compare_specs(latest.spec_json, spec) if latest else []
    change_record = None
    if latest:
        classification = "BREAKING" if any(c["classification"]=="BREAKING" for c in changes) else "WARNING" if any(c["classification"]=="WARNING" for c in changes) else "SAFE"
        change_record = ApiChange(source_id=source.id, from_version_id=latest.id, to_version_id=version.id, classification=classification, summary=f"{len(changes)} API change(s) detected", changes_json=changes)
        db.add(change_record); db.flush()
        for item in changes:
            if "path" not in item: continue
            analysis = analyze_change(item)
            impacts = find_impacts(db, source.id, item) or [None]
            for dep in impacts:
                db.add(ImpactReport(change_id=change_record.id, affected_service=dep.affected_service if dep else "Unknown", file_path=dep.file_path if dep else "Unknown", impact_level=analysis["impact_level"], explanation=analysis["explanation"], recommendation=analysis["recommendation"], status="HUMAN_REVIEW" if analysis["human_review"] else "OPEN"))
    source.last_hash = spec_hash
    db.commit()
    return {"changed":latest is not None,"version":version.version_number,"changes_detected":len(changes),"classification":change_record.classification if change_record else "INITIAL","changes":changes}
