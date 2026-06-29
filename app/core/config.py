from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Job Analyser"
    debug: bool = True
    database_url: str

    model_config = {"env_file": ".env"}

settings = Settings()
