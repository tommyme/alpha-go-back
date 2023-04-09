from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "livemodel" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "uid" VARCHAR(50) NOT NULL
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "livemodel";"""
