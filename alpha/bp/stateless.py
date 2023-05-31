import httpx
from sanic import Request, Sanic, Websocket, response, Blueprint
from sanic.response import text, HTTPResponse, json
import alpha.model as model
import sanic
from alpha.utils import add_cors_headers, test
import os
from ._build import buildBluePrint
import alpha.config.vars as vars

bp: Blueprint = buildBluePrint(__file__)
bp.static("/sgf", "dist")

@bp.get('/sgf/list')
async def get_sgf_list(request: sanic.Request):
    data = [{"file": i, "url": f'{vars.scheme_url}/{bp.url_prefix}/sgf/{i}'} for i in os.listdir("dist")]
    return json(data, ensure_ascii=False)

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
    # 前端需要访问这个接口获得输出
    try:
        json_data = resp.json()
    except:
        _content = resp.content.decode()
        _bug = '{"code":-509,"message":"请求过于频繁，请稍后再试","ttl":1}'
        if _content.startswith(_bug):
            import json as js
            _x = _content[len(_bug):]
            json_data = js.loads(_x)
    return json(json_data)

@bp.get("/articles")
async def get_articles(request: sanic.Request):
    records = await model.ArticleModel.all()
    return json([i.toDict() for i in records])

@bp.get("/article/<id>")
async def get_article(request: sanic.Request, id):
    records = await model.ArticleModel.filter(id=id).values()
    return json(records)

def getCookie():
    import http.cookies
    cookie = http.cookies.SimpleCookie()
    s = "buvid3=FFDD56E9-FF76-D86C-DE26-24708422974117169infoc; i-wanna-go-back=-1; _uuid=F10331081C-E154-3FD4-CA4F-59DE7C6B5AE817406infoc; DedeUserID=306062555; DedeUserID__ckMd5=8a7ac316753f2294; b_ut=5; header_theme_version=CLOSE; CURRENT_PID=c3d85b80-d7a7-11ed-88c8-317f4804c0e3; rpdid=|(J|)lk|lJ)u0J'uY)uuJlu|Y; buvid_fp_plain=undefined; home_feed_column=5; nostalgia_conf=-1; FEED_LIVE_VERSION=V8; CURRENT_QUALITY=80; i-wanna-go-feeds=-1; LIVE_BUVID=AUTO6816812998878297; CURRENT_FNVAL=4048; fingerprint=b21328ff229865f45e62a8701d87028f; buvid_fp=b21328ff229865f45e62a8701d87028f; hit-new-style-dyn=0; hit-dyn-v2=1; b_nut=1684034543; PVID=1; SESSDATA=6624e4ce,1700803386,91b19*52; bili_jct=57a5b0c8fccbe573b80b7933ea646db7; sid=57j8gu1c; b_lsid=B4C519107_188679D6C15; bp_video_offset_306062555=801126544744382500; innersign=0; buvid4=9BD3729B-6409-0CC1-444A-D2DB3F711FB017910-023041021-ydify6rEqFT418hRkL73qw=="
    cookie.load(s)

    res = {k:v.value for k, v in cookie.items()}
    return res

# 让管理员获取直播数据
@bp.get("/live")
async def get_live(request: sanic.Request):
    headers = {}
    headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    headers['cookies'] = "buvid3=FFDD56E9-FF76-D86C-DE26-24708422974117169infoc; i-wanna-go-back=-1; _uuid=F10331081C-E154-3FD4-CA4F-59DE7C6B5AE817406infoc; DedeUserID=306062555; DedeUserID__ckMd5=8a7ac316753f2294; b_ut=5; header_theme_version=CLOSE; CURRENT_PID=c3d85b80-d7a7-11ed-88c8-317f4804c0e3; rpdid=|(J|)lk|lJ)u0J'uY)uuJlu|Y; buvid_fp_plain=undefined; home_feed_column=5; nostalgia_conf=-1; FEED_LIVE_VERSION=V8; CURRENT_QUALITY=80; i-wanna-go-feeds=-1; LIVE_BUVID=AUTO6816812998878297; CURRENT_FNVAL=4048; fingerprint=b21328ff229865f45e62a8701d87028f; buvid_fp=b21328ff229865f45e62a8701d87028f; hit-new-style-dyn=0; hit-dyn-v2=1; b_nut=1684034543; PVID=1; SESSDATA=6624e4ce,1700803386,91b19*52; bili_jct=57a5b0c8fccbe573b80b7933ea646db7; sid=57j8gu1c; b_lsid=B4C519107_188679D6C15; bp_video_offset_306062555=801126544744382500; innersign=0; buvid4=9BD3729B-6409-0CC1-444A-D2DB3F711FB017910-023041021-ydify6rEqFT418hRkL73qw=="
    records = await model.LiveModel.all().values()
    async with httpx.AsyncClient() as client:
        for id, i in enumerate(records):
            print(i)
            url = f"https://api.bilibili.com/x/space/wbi/acc/info?mid={i['uid']}&token=&platform=web&web_location=1550101&w_rid=9c5ae5161f6b36f444665f4c929937c2&wts=1685368296"
            resp = await client.get(url, headers=headers)
            # import json
            try:
                json_data = resp.json()
                print(json_data)
            except:
                print("减掉head")
                _content = resp.content.decode()
                _bug = '{"code":-509,"message":"请求过于频繁，请稍后再试","ttl":1}'
                if _content.startswith(_bug):
                    import json as js
                    _x = _content[len(_bug):]
                    json_data = js.loads(_x)

            records[id]['name'] = json_data['data']['name']

    return json(records)

@test
@bp.get('/test')
async def test_get(request: sanic.Request):
    import time
    time.sleep(1)
    return json({
        "pid":os.getpid(),
    })

