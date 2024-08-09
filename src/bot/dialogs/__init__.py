from aiogram import Dispatcher

from .main_menu import main_menu_dialog
from .main_menu import reg_dialog


def register_dialogs(dp: Dispatcher):
    dp.include_router(main_menu_dialog)
    dp.include_router(reg_dialog)


__all__ = ['register_dialogs']