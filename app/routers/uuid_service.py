from fastapi import APIRouter
import uuid

router = APIRouter(prefix="/uuid", tags=["UUID"])

@router.get("/generate")
async def generate_uuid():
	return {"uuid": str(uuid.uuid4())}
