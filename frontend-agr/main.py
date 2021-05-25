import os
from collections import defaultdict

import requests as r
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


AUTHORS_URL = os.getenv("AUTHORS_URL", "http://bff-authors-service")
BOOKS_URL = os.getenv("BOOKS_URL", "http://bff-books-service")


def details(request):
    authors_resp = r.get(f"{AUTHORS_URL}/api/authors/")
    if authors_resp.status_code != 200:
        return JSONResponse(
            content=authors_resp.json(),
            status_code=authors_resp.status_code)
    authors = authors_resp.json()

    books_resp = r.get(f"{BOOKS_URL}/api/books/")
    if authors_resp.status_code != 200:
        return JSONResponse(
            content=books_resp.json(),
            status_code=books_resp.status_code)
    books = books_resp.json()

    books_by_author_id = defaultdict(list)
    for b in books:
        books_by_author_id[b["author_id"]].append(b)

    for a in authors:
        a["books"] = books_by_author_id.get(a["id"], [])

    return JSONResponse(authors)


routes = [Route('/frontend/api/v1/details', details)]
app = Starlette(routes=routes)
