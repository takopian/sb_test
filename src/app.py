from aiohttp import web
from aiohttp.web_response import json_response
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware
from marshmallow import ValidationError

from deposit.api import DepositView


@web.middleware
async def error_handler_middleware(request, handler):
    try:
        return await handler(request)
    except ValidationError as e:
        return json_response({"error": e.messages}, status=400)
    except Exception as e:
        return json_response({"error": str(e)}, status=500)


async def error_callback(error, *args, **kwargs):
    raise error


def create_app(argv):
    middlewares = [
        error_handler_middleware,
        validation_middleware,
    ]
    app = web.Application(middlewares=middlewares)
    app.add_routes(
        [
            web.view('/deposit', DepositView)
        ],
    )
    setup_aiohttp_apispec(
        app=app, swagger_path="/api/docs", error_callback=error_callback
    )
    return app
