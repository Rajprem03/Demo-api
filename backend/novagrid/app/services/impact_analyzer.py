from sqlalchemy.orm import Session
from app.models.dependency import Dependency

def path_matches(pattern: str, actual: str) -> bool:
    a, b = pattern.rstrip("/").split("/"), actual.rstrip("/").split("/")
    if len(a) != len(b): return False
    return all(x == y or (x.startswith("{") and x.endswith("}")) for x, y in zip(a, b))

def find_impacts(db: Session, source_id: int, change: dict):
    deps = db.query(Dependency).filter(Dependency.source_id == source_id).all()
    return [d for d in deps if (d.method == "*" or d.method.upper() == change.get("method", "").upper()) and path_matches(d.path_pattern, change.get("path", ""))]
