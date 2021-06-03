import asyncio
import json

import websockets

from app.config import GATEWAY_SERVICE_WS_URL, AUTHORS_AUTH_TOKEN, CLIENT_TYPE
from app.processor import MessageHandler


async def consumer() -> None:
    async with websockets.connect(
            f"{GATEWAY_SERVICE_WS_URL}/", extra_headers={"authorization": AUTHORS_AUTH_TOKEN}) as websocket:
        async for message in websocket:
            resp = await MessageHandler(CLIENT_TYPE, json.loads(message)).handle()
            print(resp)


if __name__ == "__main__":
    asyncio.run(consumer())
