from dataclasses import dataclass
from environs import Env



@dataclass
class TgBot:
    token: str
    use_redis: bool


@dataclass
class Db:
    host: str
    password: str
    user: str
    database: str
    port: str


@dataclass
class Misc:
    other_params: str = None


@dataclass
class Config:
    bot: TgBot
    db: Db
    misc: Misc


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        bot=TgBot(
            token=env.str("BOT_TOKEN"),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=Db(
            host=env.str("DATABASE_HOST"),
            password=env.str("DATABASE_PASSWORD"),
            user=env.str("DATABASE_USER"),
            database=env.str("DATABASE_NAME"),
            port=env.str("DATABASE_PORT"),
        ),
        misc=Misc()
    )
