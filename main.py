import os
import re
import logging
import Config
import DB
from hashlib import md5
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, ChatAction)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, RegexHandler)


co_photography_btn = KeyboardButton(text='Совместная фотография')
pleasant_memory_btn = KeyboardButton(text='Приятное воспоминание..')
lets_do_btn = KeyboardButton(text='А давай..')
keyboard = ReplyKeyboardMarkup([[co_photography_btn, pleasant_memory_btn], [lets_do_btn]], one_time_keyboard=False)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

psw = '5e3eb3b857cd9b632eee0ab852258039'

VERIFY, CHOOSING = range(2)
Elizabeth_id = None

def pleasant_memory(bot, update):
    update.message.reply_text(update.message.text + 'memory')
    return CHOOSING

def co_photography(bot, update):
    bot.send_photo(update.message.chat_id, DB.get_random_co_photography())
    return CHOOSING

def lets_do(bot, update):
    update.message.reply_text(update.message.text + 'letsdo')
    return CHOOSING

def present(bot, update):
    text = update.message.text
    logger.info(text)
    if text == 'Совместная фотография':
        co_photography(bot, update)
    elif text == 'Приятное воспоминание..':
        pleasant_memory(bot, update)
    elif text == 'А давай..':
        lets_do(bot, update)
    
    return CHOOSING


def verify_Elizabeth(bot, update):
    m = md5()
    m.update(update.message.text.encode('utf-8'))
    if m.hexdigest() == psw:
        update.message.reply_text('Верно! А теперь выбирай!', reply_markup=keyboard)
        Elizabeth_id = update.effective_user.id
        logger.info(str(Elizabeth_id))
        return CHOOSING
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
            CHOOSING: [RegexHandler('^(Совместная фотография|Приятное воспоминание..|А давай..)$',
                                    present)]
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