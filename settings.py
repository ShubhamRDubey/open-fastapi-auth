import environ
from pathlib import Path

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent
environ.Env.read_env(BASE_DIR / ".env")

SQL_SERVER = env("SQL_SERVER", cast=str)
SQL_USER = env("SQL_USER", cast=str)
SQL_PASSWORD = env("SQL_PASSWORD", cast=str)
SQL_DATABASE = env("SQL_DATABASE", cast=str)

ACCESS_TOKEN_EXPIRE_MINUTES = env("ACCESS_TOKEN_EXPIRE_MINUTES", default=24, cast=int)
REFRESH_TOKEN_EXPIRE_MINUTES = env("REFRESH_TOKEN_EXPIRE_MINUTES", default=7, cast=int)
SECRET_KEY = env("SECRET_KEY", default="insecure-secret-key", cast=str)
ALGORITHM = env("ALGORITHM", default="HS256", cast=str)
