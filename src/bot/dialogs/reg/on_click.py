from aiogram.types import Message, User
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode

from src.db.quiz_user import QuizUserDAL
from src.db.quiz_user import QuizUserORM
from src.bot.states import Reg
# from .getters import 


async def close(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager
):
    await manager.done()

# База данных
dal = QuizUserDAL()

async def start(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    

async def commit_data(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    await registrations.commit_session()

async def process_school(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode=ShowMode.EDIT
    await registrations.set_school(message.text)
    await message.delete()
    await manager.switch_to(Reg.parallel)

async def process_parallel(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode=ShowMode.EDIT
    await registrations.set_parallel(message.text)
    await message.delete()
    await manager.switch_to(Reg.check)