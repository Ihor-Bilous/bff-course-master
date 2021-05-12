import json
import typing
from enum import Enum

import aiohttp

from .config import AUTHORS_SERVICE_URL, AUTHORS_AUTH_TOKEN


class MessageType(Enum):
    BOOK = "book"
    AUTHOR = "author"


def get_message_type(message: typing.Dict) -> typing.Optional[MessageType]:
    if "author_id" in message:
        return MessageType.BOOK
    elif "first_name" in message:
        return MessageType.AUTHOR
    else:
        return None


async def get_author(author_id: int) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{AUTHORS_SERVICE_URL}/{author_id}",
            headers={
                "Authorization": AUTHORS_AUTH_TOKEN
            }
        ) as resp:
            author = await resp.json()
            return author


class WebBookMessageFormatter:
    def __init__(self, author: dict) -> None:
        self.author = author

    def format(self, message: dict) -> str:
        return f"Book: {json.dumps(message)}, Author: {json.dumps(self.author)}"


class WebAuthorMessageFormatter:
    def format(self, message: dict) -> str:
        return f"Author: {json.dumps(message)}"


class MobileBookMessageFormatter:
    def __init__(self, author: dict) -> None:
        self.author = author

    def format(self, message: dict) -> str:
        return f"Book title: {message['title']}, Author name: {self.author['first_name']} {self.author['last_name']}"


class MobileAuthorMessageFormatter:
    def format(self, message: dict) -> str:
        return f"Author name: {message['first_name']} {message['last_name']}"


class MessageHandler:
    def __init__(self, client_type, message: dict) -> None:
        self.client_type = client_type
        self.message = message

    async def handle(self) -> str:
        msg_type = get_message_type(self.message)

        if msg_type == MessageType.BOOK:
            author = await get_author(self.message["author_id"])
            formatter = self._get_book_formatter_cls()
            return formatter(author).format(self.message)
        elif msg_type == MessageType.AUTHOR:
            formatter = self._get_author_formatter_cls(self.client_type)
            return formatter().format(self.message)
        else:
            return "Unknown entity type"

    def _get_book_formatter_cls(self):
        if self.client_type == "WEB":
            return WebBookMessageFormatter
        elif self.client_type == "MOBILE":
            return MobileBookMessageFormatter
        raise Exception


    def _get_author_formatter_cls(self):
        if self.client_type == "WEB":
            return WebAuthorMessageFormatter
        elif self.client_type == "MOBILE":
            return MobileAuthorMessageFormatter
        raise Exception
