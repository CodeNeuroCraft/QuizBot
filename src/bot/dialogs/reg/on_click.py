from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode

from src.db.repos import QuizUserRepo
from src.bot.states import Reg


async def close(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager
):
    await manager.done()

# База данных
repo = QuizUserRepo()

async def start(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    manager.dialog_data['user_input'] = {
        'id': callback.message.from_user.id,
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
    await repo.new(manager.dialog_data['user_input'])

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