from sanic import Sanic
from tortoise.contrib.sanic import register_tortoise
from sanic_ext import Config
from alpha.config.tortoise import TORTOISE_ORM
import alpha.config.vars as vars

app = Sanic("hello")
app.extend(config=Config(cors=True, cors_origins='*', cors_methods="GET,POST"))
import alpha.bp
app.blueprint(alpha.bp.state.bp)
app.blueprint(alpha.bp.admin.bp)
app.blueprint(alpha.bp.stateless.bp)

register_tortoise(
    app, config=TORTOISE_ORM, generate_schemas=True, 
)

if __name__ == '__main__':
    app.run(host=vars.host, port=vars.port, dev=True, workers=3)