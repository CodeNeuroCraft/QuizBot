from pydantic import SecretStr
from pydantic_settings import BaseSettings
from sqlalchemy.engine import URL


class BotConfig(BaseSettings):
    token: SecretStr


class DBConfig(BaseSettings):
    driver: str
    user: str
    password: SecretStr
    host: str
    port: int
    name: str

    def build_connection_str(self) -> str:
        return URL.create(
            drivername=self.driver,
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.name,
        ).render_as_string(hide_password=False)


class Config(BaseSettings):
    bot: BotConfig
    db: DBConfig
# todo: add scheduler?


__all__ = ['BotConfig', 'DBConfig', 'Config']