import asyncio

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from app.api.api import api_router
from app.api.notifier import notifier
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_ENDPOINT}/openapi.json")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await notifier.connect(websocket)
    try:
        while True:
            await asyncio.sleep(0)
    except WebSocketDisconnect:
        notifier.remove(websocket)


@app.on_event("startup")
async def startup() -> None:
    await notifier.generator.asend(None)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Log</title>
    </head>
    <body>
        <h1>WebSocket Log</h1>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8080/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
        </script>
    </body>
</html>
"""


@app.get("/")
async def get() -> HTMLResponse:
    return HTMLResponse(html)


app.include_router(api_router, prefix=settings.API_ENDPOINT)
