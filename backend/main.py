from fastapi import FastAPI

from app.config import settings
from app.routes.health import router as health_router


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "AI Customer Recovery API"}