import json
import redis

from typing import Dict, Any

from app.core.config import settings


channel = "notifications"
r_connection = redis.StrictRedis.from_url(settings.REDIS_URL, decode_responses=True)


def send_push(message: Dict[Any, Any]) -> None:
    """
    Send push notification to push notification service.
    """
    r_connection.publish(channel, json.dumps(message))
