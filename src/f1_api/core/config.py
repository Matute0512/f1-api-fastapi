from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables or .env file.
    """

    project_name: str = "F1 REST API"
    database_url: str = "sqlite+aiosqlite:///./f1_local.db"

    # This tells Pydantic to look for a .env file in the root directory
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


# We create a single instance of the settings to use throughout the app.
settings = Settings()
