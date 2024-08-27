from pydantic import SecretStr
from pydantic_settings import BaseSettings


class BotConfig(BaseSettings):
    token: SecretStr


class Config(BaseSettings):
    bot: BotConfig
    temp_chat_id: int
    start_scheduler: bool
    interval_s: int


__all__ = ['BotConfig', 'Config']