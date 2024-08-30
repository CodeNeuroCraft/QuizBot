from aiogram import Dispatcher

from .database import DatabaseMiddleware


def register_middlewares(dp: Dispatcher) -> None:
    dp.message.outer_middleware(DatabaseMiddleware())
    dp.callback_query.outer_middleware(DatabaseMiddleware())


__all__ = ['register_middlewares']