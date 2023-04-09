from tortoise import Model, fields
from alpha.model.util import BetterModel

class ChatMsgModel(BetterModel):
    id = fields.IntField(pk=True)
    userId = fields.CharField(50, required=True)
    msg = fields.TextField(required=True)
    toId = fields.CharField(100, required=True)
    time = fields.DatetimeField(auto_now_add=True, required=True)

    def __str__(self):
        return f"chatmsg table item: {id}"
    


