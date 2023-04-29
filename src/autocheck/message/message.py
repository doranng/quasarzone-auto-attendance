import logging
from datetime import datetime
import telegram
from src.config import token
import asyncio


class Message:

    def send_message(self, user, results):
        now = datetime.now()

        for result in results:
            if result['result'] == 'fail':
                message = now.strftime('%Y-%m-%d %H:%M:%S') + '\n' + \
                          result['netloc'] + '/users/attendance' + '\n' + result['msg']
                asyncio.run(self.__send_telegram_message(user.telegram_id, message))

    @staticmethod
    async def __send_telegram_message(telegram_id, message):
        if telegram_id is None:
            logging.warning('Telegram ID is None')
            return

        try:
            bot = telegram.Bot(token)
            await bot.sendMessage(chat_id=telegram_id, text=message)
        except Exception:
            raise
