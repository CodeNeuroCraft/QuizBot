from typing import Dict

from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode

from src.bot.states import Reg
from src.db.database import Database


async def close(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager
):
    await manager.done()

async def start(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    manager.dialog_data['user_input'] = {
        'user_id': callback.from_user.id,
        'school': None,
        'parallel': None,
    }

async def abort(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    manager.dialog_data.clear()

async def commit(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    db: Database = manager.middleware_data['db']
    input: Dict = manager.dialog_data['user_input']

    await db.quiz_user.new(
        input['user_id'],
        input['school'],
        input['parallel'],
    )

async def process_school(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode = ShowMode.EDIT
    manager.dialog_data['user_input']['school'] = message.text
    await message.delete()
    await manager.switch_to(Reg.parallel)

async def process_parallel(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode = ShowMode.EDIT
    manager.dialog_data['user_input']['parallel'] = message.text
    await message.delete()
    await manager.switch_to(Reg.check)