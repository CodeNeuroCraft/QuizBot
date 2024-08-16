from os import getenv

from sqlalchemy import event
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine


engine = create_async_engine(
    'postgresql+asyncpg://admin:5DMG1!~Q1c7YRYP@homeserver:5432/quiz_accounts',
    future=True,
)