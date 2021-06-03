import asyncio
from typing import List

import websockets
from starlette.websockets import WebSocket, WebSocketDisconnect

from app.core.auth import check_authentication
from app.core.config import PUSH_SERVICE_WS_URL


class ConnectionsManager:
    def __init__(self) -> None:
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        self.connections.remove(websocket)

    async def broadcast(self, message: str) -> None:
        for connection in self.connections:
            await connection.send_text(message)


async def consumer() -> None:
    async with websockets.connect(f"{PUSH_SERVICE_WS_URL}/ws") as websocket:
        async for message in websocket:
            await manager.broadcast(message)


async def handler(scope, receive, send):
    websocket = WebSocket(scope=scope, receive=receive, send=send)

    if not check_authentication(websocket):
        return await websocket.close()

    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(0)
    except WebSocketDisconnect:
        manager.disconnect(websocket)


manager = ConnectionsManager()
