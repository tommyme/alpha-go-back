from tortoise import Model, fields
from alpha.model.util import BetterModel

class LiveModel(BetterModel):
    id = fields.IntField(pk=True)
    uid = fields.CharField(50, required=True)

    def __str__(self):
        return f"live table item: {id}"
    


