from os import getenv

from aiogram import Bot
from sulguk import AiogramSulgukMiddleware


async def setup_bot() -> Bot:
    
    bot: Bot = Bot(token=getenv('TOKEN'))

    # https://github.com/Tishka17/sulguk#example-for-aiogram-users
    bot.session.middleware(AiogramSulgukMiddleware())

    await bot.delete_my_commands()

    return bot


__all__ = ['setup_bot']