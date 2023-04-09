

from collections import namedtuple
from datetime import datetime
from functools import partial
import time
import sanic
from sanic_auth import Auth, User
from sanic.response import json
import alpha.model as model
from alpha.utils import hashit

UserTuple = namedtuple("UserTuple", ['id', 'name', 'admin'])

class ResponseMessage:
    NOT_ADMIN = json({"msg": 'you are not admin'}, status=403)


class CustomAuth(Auth):
    def __init__(self, app, user_keyword):
        super().__init__(app)
        self.user_keyword = user_keyword


    def from_record(self, request: sanic.Request, record: model.UserModel):
        """
        - 构建user tuple
        - 注入req.ctx.session
        - 通过哈希函数 得到sessid
        """
        user = self.build(record)
        self.login_user(request, user)
        sessid = hashit(user.name+str(time.time()))
        return sessid


    def build(self, record: model.UserModel) -> UserTuple:
        return UserTuple(id=record.userId, name=record.userName, admin=record.admin)

    def ensure_admin(self, func):
        """check admin identity"""
        async def warpper(*args, **kwargs):
            user: UserTuple = kwargs.get(self.user_keyword)
            if user.admin:
                return func(*args, **kwargs)
            else: 
                return ResponseMessage.NOT_ADMIN
        return warpper

    def Login_required(self):
        return super().login_required(user_keyword=self.user_keyword)
    


auth = CustomAuth(sanic.Sanic.get_app("hello"), 'user')
SESSIONS = {}


@auth.user_loader
def loadMyUser(token: dict):
    return UserTuple(**token)

@auth.serializer
def serializeMyUser(user: UserTuple):
    return user._asdict()

@auth.no_auth_handler
def handle_no_auth(req):
    return json({"msg": 'auth failed.'}, status=403)

async def add_session(request: sanic.Request):
    if 'sess' in request.cookies:
        # case session outdated
        if request.cookies['sess'] not in SESSIONS:
            del request.cookies['sess']
        else:
            request.ctx.session = SESSIONS[request.cookies['sess']]
            return
    request.ctx.session = {}