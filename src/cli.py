from os import getenv
from typing import Optional

import asyncclick as click
from aiogram import Bot
from aiogram import Dispatcher
from dotenv import load_dotenv

from src.bot import setup_bot
from src.bot import setup_dispatcher
from .logger import logger

async def run_bot():
    load_dotenv()

    bot: Bot = await setup_bot()

    dp: Dispatcher = setup_dispatcher()

    await logger.aerror(f"Starting bot, version: {getenv('VERSION')}")

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except (KeyboardInterrupt, SystemExit):
        await logger.error("Bot stopped!")


# @click.command()
# @click.option("--telegram_id", help="TelegramID of User", type=int)
# async def start(telegram_id: Optional[int] = None):
#     if telegram_id is not None:
#         await create_super_user(telegram_id=telegram_id)
#     else:
#         await run_bot()


__all__ = ['start']