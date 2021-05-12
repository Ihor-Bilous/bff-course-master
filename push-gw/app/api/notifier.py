from typing import Any, AsyncGenerator, Dict, List

from fastapi import WebSocket


class Notifier:
    def __init__(self) -> None:
        self.connections: List[WebSocket] = []
        self.generator = self.get_notification_generator()

    async def get_notification_generator(self) -> AsyncGenerator:
        while True:
            message = yield
            await self._notify(message)

    async def push(self, msg: Dict[str, Any]) -> None:
        await self.generator.asend(msg)

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self.connections.append(websocket)

    def remove(self, websocket: WebSocket) -> None:
        self.connections.remove(websocket)

    async def _notify(self, message: str) -> None:
        alive_connections = []
        while len(self.connections) > 0:
            websocket = self.connections.pop()
            await websocket.send_json(message)
            alive_connections.append(websocket)
        self.connections = alive_connections


notifier = Notifier()
