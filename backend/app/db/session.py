from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv

env_path = Path(__file__).resolve().parent.parent.parent / '.env'

load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessonLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessonLocal()
    try:
        yield db
    finally:
        db.close()