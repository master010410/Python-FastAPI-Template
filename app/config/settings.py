from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    port: int = 5000
    host: str = "127.0.0.1"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
