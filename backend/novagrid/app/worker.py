import time
from app.database.connection import SessionLocal
from app.models.api_source import ApiSource
from app.services.scanner import scan_source

INTERVAL=300

def scan_all():
    db=SessionLocal()
    try:
        for source in db.query(ApiSource).filter(ApiSource.active.is_(True)).all():
            try:
                print(source.name, scan_source(db, source)["classification"])
            except Exception as exc:
                db.rollback(); print("scan failed:", exc)
    finally:
        db.close()

def main():
    while True:
        scan_all(); time.sleep(INTERVAL)

if __name__ == "__main__": main()
