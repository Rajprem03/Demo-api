from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "NovaGrid"
    debug: bool = True
    database_url: str
    test_command: str = "pytest -q"
    test_timeout_seconds: int = 120
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
