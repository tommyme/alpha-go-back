import os
from sanic import Request, Sanic, Websocket, response, Blueprint


def buildBluePrint(file) -> Blueprint:
    name = os.path.basename(file).split(".")[0]
    return Blueprint(name, url_prefix=name)
