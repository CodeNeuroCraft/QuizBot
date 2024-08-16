from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.memory import SimpleEventIsolation
from aiogram_dialog import setup_dialogs

from ..dialogs import register_dialogs
from ..handlers import register_handlers


def setup_dispatcher() -> Dispatcher:
    
    dp: Dispatcher = Dispatcher(
        storage=MemoryStorage(),
        events_isolation=SimpleEventIsolation(),
    )

    register_handlers(dp=dp)
    register_dialogs(dp=dp)
    setup_dialogs(dp)

    return dp


__all__ = ['setup_dispatcher']