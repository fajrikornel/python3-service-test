from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_name: str
    db_port: int = 5432
    db_username: str
    db_password: str

    app_name: str
    app_port: int


settings = Settings(_env_file=".env")
