from aiogram.types import Message, User
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode

from src.bot.states import Reg


        
    
async def close(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager
):
    await manager.done()

# База данных
registrations = userDB()

async def start(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    await registrations.open_session(callback.from_user)

async def abort(
        callback: CallbackQuery,
        button: Button,
        manager: DialogManager,
):
    await registrations.abort_session()

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