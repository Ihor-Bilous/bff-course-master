import json
import requests as r


from starlette.requests import Request
from starlette.responses import Response

from app.core.auth import check_authentication
from app.core.config import AUTHORS_BASE_URL, BOOKS_BASE_URL, FRONTEND_BASE_URL


class ResponseGenerator:

    @staticmethod
    def forbidden():
        return Response(
            json.dumps({"detail": "forbidden"}),
            status_code=403,
            media_type="application/json"
        )

    @staticmethod
    def not_found():
        return Response(
            json.dumps({"detail": "not_found"}),
            status_code=404,
            media_type="application/json"
        )

    @staticmethod
    def method_not_allowed():
        return Response(
            json.dumps({"detail": "method_not_allowed"}),
            status_code=405,
            media_type="application/json"
        )


class ServiceRequestPreparation:

    def __init__(self, request):
        self.request = request

    async def __call__(self):
        url = self._prepare_service_url()
        kwargs = await self._prepare_request_kwargs()
        return url, kwargs

    async def _prepare_request_kwargs(self):
        kwargs = {}

        req_headers = dict(self.request.headers)
        del req_headers["authorization"]
        kwargs["headers"] = req_headers

        req_body = await self.request.body()
        if req_body:
            kwargs["data"] = req_body

        return kwargs

    def _prepare_service_url(self):
        if self.request.url.path.startswith("/api/authors"):
            return f"{AUTHORS_BASE_URL}{self.request.url.path}"
        elif self.request.url.path.startswith("/api/books"):
            return f"{BOOKS_BASE_URL}{self.request.url.path}"
        elif self.request.url.path.startswith("/frontend"):
            return f"{FRONTEND_BASE_URL}{self.request.url.path}"


async def handler(scope, receive, send):
    request = Request(scope, receive)

    if not check_authentication(request):
        return await ResponseGenerator.forbidden()(scope, receive, send)

    service_url, service_req_kwargs = await ServiceRequestPreparation(request)()

    if not service_url:
        return await ResponseGenerator.not_found()(scope, receive, send)

    service_req_method = getattr(r, request.method.lower(), None)
    if not service_req_method:
        return await ResponseGenerator.method_not_allowed()(scope, receive, send)

    service_response = service_req_method(
        service_url, **service_req_kwargs
    )

    response = Response(
        service_response.content,
        status_code=service_response.status_code,
        headers=dict(service_response.headers)
    )

    await response(scope, receive, send)
