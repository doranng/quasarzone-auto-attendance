import logging
from datetime import datetime
import telegram
from telegram.error import BadRequest
from autocheck.message.MessagePool import MessagePool
from autocheck.message.config import token
import asyncio


class Messenger:

    def send_messages(self, user):
        messages = MessagePool().get_messages()
        asyncio.run(self.__send_telegram_message(user.telegram_id, messages))
        MessagePool().clear_messages()

    @staticmethod
    async def __send_telegram_message(chat_id, messages):
        if chat_id is None:
            logging.warning('Telegram Chat ID is None')
            return

        try:
            bot = telegram.Bot(token)
            for message in messages:
                if message['result'] == 'fail':
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    text = timestamp + '\n' + message['netloc'] + '/users/attendance' + '\n' + message['msg']
                    await bot.sendMessage(chat_id=chat_id, text=text)
        except BadRequest:
            raise BadRequest
