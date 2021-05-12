from typing import Dict, Any

import requests

from app.core.config import settings


def send_push(message: Dict[Any, Any]) -> None:
    """
    Send push notification to push notification service.
    """
    notification_url = settings.NOTIFICATION_URL
    if notification_url:
        data = {"message": message}
        response = requests.post(notification_url, json=data)
        response.raise_for_status()
