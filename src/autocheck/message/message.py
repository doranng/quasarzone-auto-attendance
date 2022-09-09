import logging
from datetime import datetime
import telegram
from decouple import config, UndefinedValueError


class Message:

    def send_message(self, user, results):
        now = datetime.now()

        for result in results:
            if result['result'] == 'fail':
                message = now.strftime('%Y-%m-%d %H:%M:%S') + '\n' + \
                          result['netloc'] + '/users/attendance' + '\n' + result['msg']
                self.__send_telegram_message(user.telegram_id, message)

    @staticmethod
    def __send_telegram_message(telegram_id, message):
        if telegram_id is None:
            logging.warning('Telegram ID is None')
            return

        try:
            token = config('TOKEN')  # .env
        except UndefinedValueError:
            return

        try:
            bot = telegram.Bot(token)
            res = bot.sendMessage(chat_id=telegram_id, text=message)
            return res
        except Exception:
            raise
