from fastapi import APIRouter, Depends
from src.api.db.session import get_session
from sqlmodel import Session
from src.api.db.config import DATABASE_URL
from .models import (
    EventModel, 
    EventListSchema, 
    EventCreateSchema,
    EventUpdateSchema
)

router = APIRouter()

# GET
# List view
# GET /api/events/ -> list of events
@router.get("/")
def read_events() -> EventListSchema:
    return EventListSchema(events=[EventModel(id=1), EventModel(id=2), EventModel(id=3)])

# GET
# Individual view
# GET /api/events/{event_id} -> event details
@router.get("/{event_id}")
def read_event(event_id: int) -> EventModel:
    return EventModel(id=event_id)


# POST
# Create view
# POST /api/events/ -> create event
@router.post("/")
def create_event(payload: EventCreateSchema) -> EventModel:

    print (payload.page)
    data = payload.model_dump() # payload -> dict -> pydantic
    return EventModel(id=123, **data)


#PUT
@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventModel:
    print(payload.description)
    return EventModel(id=event_id)