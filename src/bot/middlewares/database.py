from collections.abc import Awaitable
from collections.abc import Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.structures.transfer_data import TransferData
from src.db.database import Database


class DatabaseMiddleware(BaseMiddleware):
    '''This middleware throws a Database class to handler.'''

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: TransferData,
    ) -> Any:
        async with AsyncSession(data['engine']) as session:
            data['db'] = Database(session)
            return await handler(event, data)