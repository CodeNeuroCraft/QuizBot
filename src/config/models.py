from typing import Optional

from pydantic import SecretStr
from pydantic_settings import BaseSettings
from sqlalchemy.engine import URL


class BotConfig(BaseSettings):
    token: SecretStr


class DBConfig(BaseSettings):
    driver: Optional[str]
    user: Optional[str]
    password: SecretStr
    host: Optional[str]
    port: Optional[int]
    name: Optional[str]

    def build_connection_str(self) -> str:
        return URL.create(
            drivername=self.driver,
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.name,
        ).render_as_string(hide_password=False)


class Config(BaseSettings):
    bot: BotConfig
    db: DBConfig
# todo: add scheduler?


__all__ = ['BotConfig', 'DBConfig', 'Config']