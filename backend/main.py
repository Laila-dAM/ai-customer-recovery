from fastapi import FastAPI

from app.config import settings
from app.routes.health import router as health_router
from app.routes.auth.register import router as register_router


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(health_router)
app.include_router(register_router, prefix="/auth")


@app.get("/")
def root():
    return {"message": "AI Customer Recovery API"}