import asyncio
from starlette.applications import Starlette

from app.handlers import http
from app.handlers import ws


conn_type_handlers = {
    "http": http.handler,
    "websocket": ws.handler
}


class APIGatewayApp:

    async def __call__(self, scope, receive, send):
        conn_handler = conn_type_handlers[scope["type"]]
        await conn_handler(scope, receive, send)


asgi_app = APIGatewayApp()

app = Starlette()

app.mount('/', asgi_app)


@app.on_event("startup")
async def startup():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(ws.consumer(), loop=loop)
