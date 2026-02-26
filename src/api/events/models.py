# from pydantic import BaseModel, Field
from sqlmodel import SQLModel, Field
from typing import List


class EventModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    page: str | None = None
    description: str | None = Field(default=None, max_length=255)

class EventCreateSchema(SQLModel):
    page: str
    description: str | None = Field(default=None, max_length=255)



class EventUpdateSchema(SQLModel):
    description: str



class EventListSchema(SQLModel):
    events: list[EventModel] ## List[EventSchema]