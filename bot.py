import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from tg_bot.config import load_config
from tg_bot.handlers.echo import register_echo

logger = logging.getLogger(__name__)


def register_all_middlewares(dp):
    ...


def register_all_filters(dp):
    ...


def register_all_handlers(dp):
    register_echo(dp)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    config = load_config('.env')

    bot = Bot(token=config.bot.token, parse_mode='HTML')
    storage = RedisStorage2() if config.bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    register_all_middlewares(dp)
    register_all_filters(dp)
    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
        logger.info('Bot started!')
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')
