import os
import asyncio
import json

import websockets

from app.config import NOTIFICATION_WS_URL
from app.processor import MessageHandler


CLIENT_TYPE = os.getenv("CLIENT_TYPE", "WEB")
if CLIENT_TYPE not in ["WEB", "MOBILE"]:
    raise Exception("Unknown client type")


async def consumer() -> None:
    async with websockets.connect(NOTIFICATION_WS_URL) as websocket:
        async for message in websocket:
            resp = await MessageHandler(CLIENT_TYPE, json.loads(message)).handle()
            print(resp)


if __name__ == "__main__":
    asyncio.run(consumer())
