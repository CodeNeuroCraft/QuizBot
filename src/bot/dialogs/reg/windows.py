from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.input import MessageInput

from src.bot.states import Reg
from .on_event import *
from .getters import *


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
        Const('Введите ваш класс:'),
        Row(
            Button(
                Const('8'),
                id='8_grade',
            ),
            Button(
                Const('9'),
                id='9_grade',
            ),
        ),
        MessageInput(process_parallel, content_types=[ContentType.TEXT]),
        state=Reg.grade,
        markup_factory=ReplyKeyboardFactory(
            resize_keyboard=True,
            one_time_keyboard=True,
        ),
    )

def check_window():
    return Window(
        Const('Введенные данные:'),
        Format('Школа: {school}'),
        Format('Класс: {grade}'),
        Row(
            SwitchTo(
                Const('ВСЁ ВЕРНО'),
                id='success',
                state=Reg.success,
                on_click=commit,
            ),
            SwitchTo(
                Const('ХРЕНЬ'),
                id='confirm',
                state=Reg.confirm,
                on_click=abort,
            ),
        ),
        getter=check_window_getter,
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