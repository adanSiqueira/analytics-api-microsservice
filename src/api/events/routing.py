from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_events():
    return {"message": "Events endpoint"}

@router.get("/{event_id}")
def read_event(event_id: str):
    return {"event_id": event_id}