from sqlalchemy import create_engine
from config import config


def get_url():
    username = config.settings.db_username
    password = config.settings.db_password
    host = config.settings.db_host
    port = config.settings.db_port
    db = config.settings.db_name
    return f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"


engine = create_engine(get_url())


def get_engine():
    return engine
