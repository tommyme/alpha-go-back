from collections import namedtuple
from sanic import Request, Sanic, Websocket, response, Blueprint
from sanic.response import text, HTTPResponse, json
from tortoise.contrib.sanic import register_tortoise
import alpha.model as model
from datetime import datetime
import sanic
from alpha.utils import add_cors_headers, hashit
from functools import partial
from ._auth import auth, UserTuple
from ._build import buildBluePrint

bp: Blueprint = buildBluePrint(__file__)


@bp.post("/articles/add")
@auth.Login_required()
@auth.ensure_admin
async def articleAdd(request: Request, user):
    pass


@bp.post("/live/add")
@auth.Login_required()
@auth.ensure_admin
async def liveAdd(request: Request, user):
    pass

