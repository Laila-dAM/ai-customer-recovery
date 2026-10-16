
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Customer Recovery"
    app_version: str = "0.1.0"
    debug: bool = True
    database_url: str = "sqlite:///./ai_customer_recovery.db"


settings = Settings()
