"""Database class with all-in-one features."""

from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine

from .repos import QuizUserRepo


def create_async_engine(url: URL | str) -> AsyncEngine:
    '''Create async engine with given URL.

    :param url: URL to connect
    :return: AsyncEngine
    '''
    return _create_async_engine(url=url, pool_pre_ping=True)


class Database:
    '''Database class is the highest abstraction level of database and
    can be used in the handlers or any others bot-side functions.'''

    user: QuizUserRepo

    session: AsyncSession

    def __init__(
        self,
        session: AsyncSession,
        user: QuizUserRepo = None,
    ):
        self.session = session
        self.user = user or QuizUserRepo(session=session)
