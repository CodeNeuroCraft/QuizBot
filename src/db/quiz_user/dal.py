import asyncio
from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from .model import QuizUserORM
from ..session import session_maker


class QuizUserDAL:
    def __init__(self, session: Optional[AsyncSession] = None):
        if session is None:
            self.__create_session()
        else:
            self.__session = session

    @staticmethod
    def __create_session(self):
        session: AsyncSession = session_maker()
        self.__session = session

    async def __del__(self):
        if self.__session:
            asyncio.create_task(self.__session.close())

    async def create_user(self, id: int, school: str, parallel: str):
        await self.__session.add(QuizUserORM(id=id, school=school, parallel=parallel))
        return await self.__session.commit()
    
    async def delete_user(self, id: int):
        await self.__session.delete(QuizUserORM(id=id))
        return await self.__session.commit()

    async def get_user(self, id: int):
        return await self.__session.get(QuizUserORM, id)


__all__ = ['QuizUserDAL']