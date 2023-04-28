from tortoise import Model, fields
from alpha.model.util import BetterModel

class RankModel(BetterModel):
    id = fields.IntField(pk=True)
    name = fields.CharField(50, required=True)
    rank = fields.IntField(required=True)
    score = fields.FloatField(required=True)

    def __str__(self):
        return f"rank table item: {id}"
    


