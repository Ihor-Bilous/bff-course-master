import os

NOTIFICATION_WS_URL = os.getenv("NOTIFICATION_WS_URL", "ws://bff-push-service/ws")
AUTHORS_SERVICE_URL = os.getenv("AUTHORS_SERVICE_URL", "http://bff-authors-service/api/authors")
AUTHORS_AUTH_TOKEN = os.getenv("AUTHORS_AUTH_TOKEN", "")
