from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from settings import SQL_SERVER, SQL_USER, SQL_PASSWORD, SQL_DATABASE

encoded_password = quote(SQL_PASSWORD)

DATABASE_URL = f"mysql+mysqlconnector://{SQL_USER}:{encoded_password}@{SQL_SERVER}/{SQL_DATABASE}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class UserDB(Base):
    __tablename__ = "user_table"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
