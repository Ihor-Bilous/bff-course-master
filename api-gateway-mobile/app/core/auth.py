from .config import AUTH_TOKEN


def check_authentication(request):
    try:
        token = request.headers["authorization"]
    except KeyError:
        return False

    if token != AUTH_TOKEN:
        return False

    return True
