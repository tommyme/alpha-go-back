from tortoise import Model, fields


class BetterModel(Model):

    def toDict(self):
        return {k: self.__dict__[k] for k in self._meta.fields}