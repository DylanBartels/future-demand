from typing import Optional, List
from datetime import date, time

from sqlmodel import SQLModel, Field
from pydantic import HttpUrl


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: date
    time: time
    location: str
    title: str
    artists: List[str]
    works: List[str]
    image_link: HttpUrl
