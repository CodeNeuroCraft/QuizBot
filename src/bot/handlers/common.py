from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import StateFilter

from src.bot.states import Reg
from src.bot.states import MainMenu

common = Router()


@common.message(
        StateFilter(MainMenu.welcome | MainMenu.help | 
                    Reg.confirm | Reg.check | Reg.success)
)
async def prevent_typing(message: Message, state: FSMContext, **kwargs):
    await message.delete()


__all__ = ['router']