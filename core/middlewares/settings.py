from environs import Env
from dataclasses import dataclass


@dataclass
class BotConfig:
    bot_token: str
    https: str
    api: str


@dataclass
class Settings:
    bot_config: BotConfig


def get_settings(path: str):
    env = Env()
    env.read_env(path)
    return Settings(
        bot_config=BotConfig(
            bot_token=env.str('TOKEN'),
            https=env.str('HTTPS'),
            api=env.str('API')
        )
    )

settings = get_settings('settings')
