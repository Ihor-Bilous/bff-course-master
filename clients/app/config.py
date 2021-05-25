import os

GATEWAY_SERVICE_URL = os.getenv("GATEWAY_SERVICE_URL", "http://bff-api-gateway")
GATEWAY_SERVICE_WS_URL = os.getenv("GATEWAY_SERVICE_WS_URL", "ws://bff-api-gateway")
AUTHORS_AUTH_TOKEN = os.getenv("AUTHORS_AUTH_TOKEN", "")
