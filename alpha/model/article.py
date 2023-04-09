from tortoise import Model, fields
from alpha.model.util import BetterModel

class ArticleModel(BetterModel):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=50, required=True)
    content = fields.TextField(required=True)

    def __str__(self):
        return f"article table item: {id}"
    