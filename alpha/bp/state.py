from sanic import Request, Sanic, Websocket, response, Blueprint
from sanic.response import text, HTTPResponse, json
import alpha.model as model
from datetime import datetime
from alpha.utils import add_cors_headers, hashit
from functools import partial
from ._build import buildBluePrint
from ._auth import auth, add_session, SESSIONS, UserTuple
from . import _common 
from alpha.utils import test

bp: Blueprint = buildBluePrint(__file__)


bp.middleware("response")(add_cors_headers)
bp.middleware('request')(add_session)

@bp.post('/register')
async def register(request: Request):
    username = request.json['username']
    hashed_pass = hashit(request.json['password'])
    result = await model.UserModel(userName=username, password=hashed_pass).save()
    return response.json({"msg": 'success'})

@bp.post('/login')
async def login(request: Request):
    username = request.json['username']
    hashed_pass = hashit(request.json['password'])
    result = await model.UserModel.filter(userName=username, password=hashed_pass)
    if result == []:
        return json({'msg': 'auth failed'}, status=403)
    
    # 登录成功
    user_record = result[0]
    resp = response.json({
        "userId": user_record.userId, 
        "userName": user_record.userName, 
        "admin": user_record.admin})

    sessid = auth.from_record(request, user_record)
    SESSIONS[sessid] = request.ctx.session     # 存储session
    resp.cookies['sess'] = sessid
    return resp


@bp.websocket('/websocket')
@auth.Login_required()
async def do_websocket(request: Request, ws: Websocket, user: UserTuple):
    """
    接收消息 作为admin 返回消息
    """
    async for msg in ws:
        resp_msg = "[自动回复]: 您好, 客服暂时不在 您的留言我们已经收到 请您耐心等待"
        # 消息进入数据库
        await model.ChatMsgModel(userId=user.id, msg=msg, toId=_common.ADMIN_UUID).save()
        await model.ChatMsgModel(userId=_common.ADMIN_UUID, msg=resp_msg, toId=user.id).save()
        # 返回消息
        await ws.send(resp_msg)

# 需要有token
@bp.get('/messages')
@auth.Login_required()
async def get_messages(request: Request, user: UserTuple):
    """
    查询所有发送者为user 和 接受者为user的消息
    """
    # user = UserTuple(id='4bd45530-d112-44fa-88d8-eda0397f5d7f', name= 'aaa')
    history: list[model.ChatMsgModel] = await model.ChatMsgModel.filter(userId=user.id)
    history += await model.ChatMsgModel.filter(toId=user.id)
    history.sort(key=lambda x: x.time)
    # convert to timeStamp
    for i in history:
        i.time = i.time.timestamp()
    res = [i.toDict() for i in history]
    # add name info
    for i in res: 
        _query = await model.UserModel.filter(userId=i['userId']).values('userName')
        i['userName'] = _query[0]['userName']
    return json(res)


@test
@bp.websocket('/test/makews')
async def test_conn_websocket(request: Request, ws: Websocket):
    user = UserTuple(id='4bd45530-d112-44fa-88d8-eda0397f5d7f', name= 'aaa', admin=False)
    async for msg in ws:
        resp_msg = "[自动回复]: 您好, 客服暂时不在 您的留言我们已经收到 请您耐心等待"
        # 消息进入数据库
        # await model.ChatMsgModel(userId=user.id, msg=msg, toId=_common.ADMIN_UUID).save()
        # await model.ChatMsgModel(userId=_common.ADMIN_UUID, msg=resp_msg, toId=user.id).save()
        # 返回消息
        await ws.send(resp_msg)

@test
@bp.get('/test/makemsg')
async def test_get_history_messages(request: Request):
    user = UserTuple(id='4bd45530-d112-44fa-88d8-eda0397f5d7f', name= 'aaa')
    history: list[model.ChatMsgModel] = await model.ChatMsgModel.filter(userId=user.id)
    history += await model.ChatMsgModel.filter(toId=user.id)
    history.sort(key=lambda x: x.time)
    # convert to timeStamp
    for i in history:
        i.time = i.time.timestamp()
    res = [i.toDict() for i in history]
    # add name info
    for i in res: 
        _query = await model.UserModel.filter(userId=i['userId']).values('userName')
        i['userName'] = _query[0]['userName']
    return json(res)

