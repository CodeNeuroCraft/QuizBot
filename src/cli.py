from aiogram import Bot
from aiogram import Dispatcher
from sqlalchemy.ext.asyncio import AsyncEngine

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

    engine: AsyncEngine = create_async_engine(url=config.db.build_connection_str())

    await logger.ainfo(f'Starting bot, version: {VERSION}')


    await dp.start_polling(
        bot,
        **TransferData(
            engine=engine
        ),
    )