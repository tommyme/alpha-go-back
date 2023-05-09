from tortoise import Model, fields
from alpha.model.util import BetterModel

class UserModel(BetterModel):
    id = fields.IntField(pk=True)
    userId = fields.CharField(50, required=True, unique=True)  
    userName = fields.CharField(50, required=True, unique=True)
    password = fields.CharField(100, required=True)
    admin = fields.BooleanField(default=False)

    def __str__(self):
        return f"User {self.userId} {self.userName}"
