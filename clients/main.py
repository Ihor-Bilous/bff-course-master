import os
import asyncio
import json

import websockets

from app.config import GATEWAY_SERVICE_WS_URL, AUTHORS_AUTH_TOKEN
from app.processor import MessageHandler


CLIENT_TYPE = os.getenv("CLIENT_TYPE", "WEB")
if CLIENT_TYPE not in ["WEB", "MOBILE"]:
    raise Exception("Unknown client type")


async def consumer() -> None:
    async with websockets.connect(
            f"{GATEWAY_SERVICE_WS_URL}/", extra_headers={"authorization": AUTHORS_AUTH_TOKEN}) as websocket:
        async for message in websocket:
            resp = await MessageHandler(CLIENT_TYPE, json.loads(message)).handle()
            print(resp)


if __name__ == "__main__":
    asyncio.run(consumer())
