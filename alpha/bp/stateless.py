import httpx
from sanic import Request, Sanic, Websocket, response, Blueprint
from sanic.response import text, HTTPResponse, json
import alpha.model as model
import sanic
from alpha.utils import add_cors_headers, test
from ._build import buildBluePrint

bp: Blueprint = buildBluePrint(__file__)



@bp.get("/relay")      # query
async def relay_get(request: sanic.Request):
    # 把参数都发过来就行
    url = request.args.get('url')
    del request.args['url']
    # params = {k:v[0] for k, v in request.args.items()}
    headers = {}
    headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, params=request.args, headers=headers)
    return json(resp.json())

@bp.get("/articles")
async def get_articles(request: sanic.Request):
    records = await model.ArticleModel.all()
    return json([i.toDict() for i in records])

@bp.get("/article/<id>")
async def get_article(request: sanic.Request, id):
    records = await model.ArticleModel.filter(id=id).values()
    return json(records)

@bp.get("/live")
async def get_live(request: sanic.Request):
    records = await model.LiveModel.all().values()
    return json(records)

@test
@bp.get('/test')
async def test_get(request: sanic.Request):
    return text('test')

