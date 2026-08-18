from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(title=settings.app_name, version="1.0.0", description="NovaGrid: self-maintaining API backend")
app.include_router(router)

@app.get("/health", tags=["System"])
def health():
    return {"status":"ok","service":"novagrid","version":"1.0.0"}
