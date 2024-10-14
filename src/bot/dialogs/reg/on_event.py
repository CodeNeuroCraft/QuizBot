from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode

from src.bot.states import Reg
from src.db.database import Database


async def start(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    manager.dialog_data['input'] = {
        'user_id': callback.from_user.id,
        'school': None,
        'grade': None,
    }

async def restart(
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
    input_ = manager.dialog_data['input']

    await db.quiz_user.from_dict(input_)

async def process_school(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode = ShowMode.EDIT
    manager.dialog_data['input']['school'] = message.text
    await message.delete()
    await manager.switch_to(Reg.grade)

async def process_grade(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    manager.show_mode = ShowMode.EDIT
    manager.dialog_data['input']['grade'] = button.widget_id[-1]
    await callback.message.delete()
    await manager.switch_to(Reg.check)