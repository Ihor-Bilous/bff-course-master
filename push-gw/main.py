import asyncio
import json

import aioredis
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from app.api.notifier import notifier
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_ENDPOINT}/openapi.json")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await notifier.connect(websocket)
    try:
        await redis_connector()
    except WebSocketDisconnect:
        notifier.remove(websocket)


async def redis_connector():

    async def producer_handler(r):
        (channel,) = await r.subscribe("notifications")
        assert isinstance(channel, aioredis.Channel)
        while True:
            message = await channel.get()
            if message:
                await notifier.broadcast(json.loads(message.decode("utf-8")))

    redis = await aioredis.create_redis_pool(settings.REDIS_URL)

    producer_task = producer_handler(redis)
    done, pending = await asyncio.wait([producer_task, ])
    for task in pending:
        task.cancel()
    redis.close()
    await redis.wait_closed()
