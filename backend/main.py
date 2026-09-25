from fastapi import FastAPI

from app.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)


@app.get("/")
def root():
    return {"message": "AI Customer Recovery API"}