from aiogram import Dispatcher
from aiogram.filters import ExceptionTypeFilter
from aiogram_dialog.api.exceptions import UnknownIntent

from .errors import on_unknown_intent
from .common import common


def register_handlers(dp: Dispatcher) -> None:
    dp.include_router(common)

    dp.errors.register(
        on_unknown_intent,
        ExceptionTypeFilter(UnknownIntent),
    )


__all__ = ['register_handlers']