from typing import Any, Dict

from fastapi import APIRouter
from pydantic import BaseModel

from app.api.notifier import notifier

api_router = APIRouter()


class PushMessageSchema(BaseModel):
    message: Dict[Any, Any]


@api_router.post("/push")
async def push(message_in: PushMessageSchema) -> Any:
    """
    Send push notification.
    """
    await notifier.push(message_in.message)
    return {"success": True}
