import asyncio

from aiogram.types import ContentType
from aiogram_dialog import Window
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from src.bot.states import MainMenu
from src.bot.states import Reg
from .on_event import *


def welcome_window():
    return Window(
        StaticMedia(
            url='https://downloader.disk.yandex.ru/preview/a2db807363a125c36e093c96d62c51fbc6285868179286ba3e670c83f2ee2b2f/667b2587/R62WU8dtk7-Q0djji7n-cmxE-rn890DjbBvDmq6ghcaYktDbn6tkZFArOExvqcvTbhQWrZ6Z6FOTcyT3jT8zNQ%3D%3D?uid=0&filename=onwhite_ver.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x918',
            type=ContentType.PHOTO
        ),
        Const('Добро пожаловать на викторину! Выберите пункт меню:'),
        Row(
            Start(
                Const('Регистрация'),
                id='reg',
                state=Reg.confirm,
                when=check_user,
            ),
            SwitchTo(
                Const('Помощь'),
                id='help',
                state=MainMenu.help,
            ),
        ),
        state=MainMenu.welcome,
    )

def help_window():
    return Window(
        Const('Пока ничего тут нету. Но скоро появится)'),
        SwitchTo(
            Const('НАЗАД'),
            id='back',
            state=MainMenu.welcome,
        ),
        state=MainMenu.help,
    )