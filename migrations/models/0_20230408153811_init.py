from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "articlemodel" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" VARCHAR(50) NOT NULL,
    "content" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "bettermodel" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
);
CREATE TABLE IF NOT EXISTS "chatmsgmodel" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "userId" VARCHAR(50) NOT NULL,
    "msg" TEXT NOT NULL,
    "toId" VARCHAR(100) NOT NULL,
    "time" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "usermodel" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "userId" VARCHAR(50) NOT NULL UNIQUE,
    "userName" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(100) NOT NULL,
    "admin" INT NOT NULL  DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
