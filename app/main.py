from fastapi import FastAPI

app = FastAPI()

from app.routers import uuid_service
app.include_router(uuid_service.router)
