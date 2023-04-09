from tortoise import Tortoise
import alpha.model as model
import uuid
from alpha.utils import hashit
import asyncio
from alpha.config.tortoise import TORTOISE_ORM
import click

async def init():
	await Tortoise.init(
		config=TORTOISE_ORM
	)
	await Tortoise.generate_schemas()

async def main(admin: bool):
    await init()
    Model = model.UserModel
    await Model(
        userId=uuid.uuid4(), 
        userName=input('username:').strip(), 
        password=hashit(input('password:').strip()),
        admin=admin
    ).save()
    print("success")
    exit(0)

@click.command()
@click.option('--admin', is_flag=True, default=False)
def cmd(admin):
    asyncio.run(
        main(admin)
    )

if __name__ == "__main__":
    cmd()