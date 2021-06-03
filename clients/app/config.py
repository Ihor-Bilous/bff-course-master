import os

CLIENT_TYPE = os.getenv("CLIENT_TYPE", "WEB")
if CLIENT_TYPE not in ["WEB", "MOBILE"]:
    raise Exception("Unknown client type")

default_api_gateway_host_http = ""
default_api_gateway_host_ws = ""

if CLIENT_TYPE == "WEB":
    default_api_gateway_host_http = "http://bff-api-gateway-frontend"
    default_api_gateway_host_ws = "ws://bff-api-gateway-frontend"
elif CLIENT_TYPE == "MOBILE":
    default_api_gateway_host_http = "http://bff-api-gateway-mobile"
    default_api_gateway_host_ws = "ws://bff-api-gateway-mobile"

GATEWAY_SERVICE_URL = os.getenv("GATEWAY_SERVICE_URL", default_api_gateway_host_http)
GATEWAY_SERVICE_WS_URL = os.getenv("GATEWAY_SERVICE_WS_URL", default_api_gateway_host_ws)

AUTHORS_AUTH_TOKEN = os.getenv("AUTHORS_AUTH_TOKEN", "")
