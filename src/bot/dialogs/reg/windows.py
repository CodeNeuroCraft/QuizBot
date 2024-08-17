from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.input import MessageInput

from src.bot.states import Reg
from .on_click import start
from .on_click import abort
from .on_click import commit_data
from .on_click import process_school
from .on_click import process_parallel
from .on_click import close


def confirm_window():
    return Window(
        Const('Вы уверены, что хотите зарегистрироваться?'),
        Row(
            SwitchTo(
                Const('ДА'),
                id='school',
                state=Reg.school,
                on_click=start,
            ),
            Button(
                Const('НЕТ'),
                id='back',
                on_click=close,
            ),
        ),
        state=Reg.confirm,
    )

def school_window():
    return Window(
        Const('Введите вашу школу:'),
        MessageInput(process_school, content_types=[ContentType.TEXT]),
        state=Reg.school,
    )

def parallel_window():
    return Window(
        Const('Введите вашу параллель:'),
        MessageInput(process_parallel, content_types=[ContentType.TEXT]),
        state=Reg.parallel,
    )

def check_window():
    return Window(
        Const('Введенные данные:'),
        Format('Школа: {school};'),
        Format('Параллель: {parallel};'),
        Row(
            SwitchTo(
                Const('ВСЁ ВЕРНО'),
                id='success',
                state=Reg.success,
                on_click=commit_data
            ),
            SwitchTo(
                Const('ХРЕНЬ'),
                id='confirm',
                state=Reg.confirm,
                on_click=abort
            ),
        ),
        getter=on_event.registrations.get_session_data,
        state=Reg.check,
    )

def success_window():
    return Window(
        Const('Вы успешно зарегистрированы!'),
        Button(
            Const('НАЗАД'),
            id='back',
            on_click=close,
        ),
        state=Reg.success,
    )