from os import getenv

from sqlmodel import create_engine

engine = create_engine(getenv("DATABASE_URL"), echo=True)
