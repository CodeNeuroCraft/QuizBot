from aiogram import Bot
from aiogram.types import BotCommandScopeChat
from sulguk import AiogramSulgukMiddleware


async def setup_bot(
    superusers_id: list[int], users_id: list[int]
) -> Bot:
    
    bot: Bot = Bot()

    # https://github.com/Tishka17/sulguk#example-for-aiogram-users
    bot.session.middleware(AiogramSulgukMiddleware())

    await bot.delete_my_commands()

    # for _id in users_id:
    #     await bot.set_my_commands(
    #         user_commands(), scope=BotCommandScopeChat(chat_id=_id)
    #     )

    # for _id in superusers_id:
    #     await bot.set_my_commands(
    #         user_commands() + superuser_commands(),
    #         scope=BotCommandScopeChat(chat_id=_id),
    #     )

    # await bot.delete_webhook()
    return bot


__all__ = ['setup_bot']