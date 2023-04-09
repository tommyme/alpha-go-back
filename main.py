from sanic import Sanic
from tortoise.contrib.sanic import register_tortoise
from sanic_ext import Config
from alpha.config.tortoise import TORTOISE_ORM

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
    app.run(host='127.0.0.1', port=8000, debug=True)