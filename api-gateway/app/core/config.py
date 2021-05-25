import os

AUTH_TOKEN = os.getenv("AUTH_TOKEN", "")
AUTHORS_BASE_URL = os.getenv("AUTHORS_BASE_URL", "http://bff-authors-service")
BOOKS_BASE_URL = os.getenv("BOOKS_BASE_URL", "http://bff-books-service")
FRONTEND_BASE_URL = os.getenv("FRONTEND_BASE_URL", "http://bff-frontend-service")
PUSH_SERVICE_WS_URL = os.getenv("PUSH_SERVICE_WS_URL", "ws://bff-push-service")
