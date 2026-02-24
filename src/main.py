from typing import Union
from fastapi import FastAPI
from api.events import router as events_router

app = FastAPI()
app.include_router(events_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def api_health():
    return {"status": "ok"}
