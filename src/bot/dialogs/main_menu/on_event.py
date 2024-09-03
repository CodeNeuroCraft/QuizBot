from typing import Dict

from aiogram.types import User
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from src.bot.states import Reg
from src.db.database import Database


async def check_user(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    db: Database = manager.middleware_data['db']
    user: User = manager.middleware_data['event_from_user']

    if await db.quiz_user.get(user.id) == None:
        await manager.start(Reg.confirm)
    else:
        await callback.answer('мы уже в курсе о том, где ты учишься, сладенький)')


__all__ = ['check_user']