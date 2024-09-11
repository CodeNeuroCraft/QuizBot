from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import StateFilter
from aiogram_dialog import DialogManager
from aiogram_dialog import StartMode

from src.bot.states import Reg
from src.bot.states import MainMenu


common = Router()

@common.message(CommandStart())
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.welcome, mode=StartMode.RESET_STACK)


__all__ = ['common']