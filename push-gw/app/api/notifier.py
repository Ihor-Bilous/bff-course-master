from typing import List

from fastapi import WebSocket


class Notifier:
    def __init__(self) -> None:
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self.connections.append(websocket)

    def remove(self, websocket: WebSocket) -> None:
        self.connections.remove(websocket)

    async def broadcast(self, message: str) -> None:
        for connection in self.connections:
            await connection.send_json(message)


notifier = Notifier()
