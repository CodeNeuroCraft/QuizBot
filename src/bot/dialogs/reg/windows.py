from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Cancel

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
            Cancel(
                Const('НЕТ'),
                id='back',
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

def grade_window():
    return Window(
        Const('Введите ваш класс:'),
        Row(
            Button(
                Const('🎱8'),
                id='grade_8',
                on_click=process_grade,
            ),
            Button(
                Const('⚖9'),
                id='grade_9',
                on_click=process_grade,
            ),
        ),
        state=Reg.grade,
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
                Const('ЕСТЬ ОШИБКИ'),
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
        Cancel(
            Const('НАЗАД'),
            id='back',
        ),
        state=Reg.success,
    )