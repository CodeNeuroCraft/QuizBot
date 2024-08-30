from aiogram import Bot
from aiogram import Dispatcher

from src.bot import setup_bot
from src.bot import setup_dispatcher
from src.config import Config
from src.config import load_config
from src.constants import CONFIG_FILE_PATH
from src.constants import VERSION
from .logger import logger
from src.bot.structures.transfer_data import TransferData
from src.db.database import create_async_engine


async def run_bot():
    config: Config = load_config(config_path=CONFIG_FILE_PATH)

    bot: Bot = await setup_bot(config=config.bot)

    dp: Dispatcher = setup_dispatcher()

    await logger.aerror(f'Starting bot, version: {VERSION}')

    try:
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
            **TransferData(
                engine=create_async_engine(url=config.db.build_connection_str())
            ),
        )
    except (KeyboardInterrupt, SystemExit):
        await logger.error('Bot stopped!')


__all__ = ['run_bot']