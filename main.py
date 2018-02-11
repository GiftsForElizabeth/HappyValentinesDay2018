import os
import re
import logging
import Config
from hashlib import md5
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, ChatAction)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

psw = '5e3eb3b857cd9b632eee0ab852258039'

VERIFY, PRESENT = range(2)

def pleasant_memory(bot, update):
    update.message.reply_text(update.message.text + 'memory')
    return PRESENT

def co_photography(bot, update):
    update.message.reply_text(update.message.text + 'cofoto')
    return PRESENT

def present(bot, update):
    update.message.reply_text("PRESENT")
    return PRESENT

def verify_Elizabeth(bot, update):
    m = md5()
    m.update(update.message.text.encode('utf-8'))
    if m.hexdigest() == psw:
        update.message.reply_text('Верно!')
        return PRESENT
    update.message.reply_text('Возможно, ты не Лиза.. Попробуй ещё раз (или напиши Диме).')
    return VERIFY

def start(bot, update):
    update.message.reply_text('Докажи, что ты Лиза. Введи пароль:')
    return VERIFY

def main():
    """Start bot"""

    token = Config.get_token()
    port = int(os.environ.get('PORT', '5000'))
    updater = Updater(token);
    dpt = updater.dispatcher;

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            VERIFY: [MessageHandler(Filters.text, verify_Elizabeth)],
            PRESENT: [MessageHandler(Filters.text, present)]
        },

        fallbacks=[CommandHandler('start', start)]
    )
    dpt.add_handler(conv_handler)
    # dpt.add_error_handler(error)

    # env = ParseConfig.get_env()
    updater.start_polling()
    # updater.start_webhook(listen="0.0.0.0", port=port, url_path=token)
    # updater.bot.set_webhook('https://' + Config.get_url() + '.herokuapp.com/' + token)

    updater.idle()

if __name__ == '__main__':
    main()