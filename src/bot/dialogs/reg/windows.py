from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.input import TextInput

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
        state=Reg.school,
    )

def grade_window():
    return Window(
        Const('Введите ваш класс:'),
        Row(
            Button(
                Const('8'),
                id='grade_8',
                on_click=
            ),
            Button(
                Const('9'),
                id='grade_9',
            ),
        ),
        TextInput(
            id='grade',
            on_success=success_grade,
            type_factory=int,
        ),
        state=Reg.grade,
        markup_factory=ReplyKeyboardFactory(
            resize_keyboard=True,
            one_time_keyboard=True,
            is_persistent=True,
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
                on_click=restart,
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