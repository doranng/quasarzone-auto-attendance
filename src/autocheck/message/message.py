import telegram
from decouple import config


def send_message(user_data, results):
    for result in results:
        if result['result'] == 'fail':
            send_telegram_message(user_data['telegram_id'], '[' + result['netloc'] + '] ' + result['msg'])


def send_telegram_message(telegram_id, message):
    try:
        bot = telegram.Bot(config('TOKEN'))
        res = bot.sendMessage(chat_id=telegram_id, text=message)
        return res
    except Exception:
        raise
