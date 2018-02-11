import os
import re
import Config

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, ChatAction)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)

IDLE = 1

def pleasant_memory(bot, update):
    update.message.reply_text(update.message.text)
    return IDLE

def co_photography(boy, update):
    update.message.reply_text(update.message.text)
    return IDLE

def main():
    """Start bot"""

    token = Config.get_token()
    port = int(os.environ.get('PORT', '5000'))
    updater = Updater(token);
    dpt = updater.dispatcher;

    dpt.add_handler(CommandHandler('co_photography', co_photography))

    # dpt.add_error_handler(error)

    # env = ParseConfig.get_env()
    updater.start_webhook(listen="0.0.0.0", port=port, url_path=token)
    updater.bot.set_webhook('https://' + Config.get_url() + '.herokuapp.com/' + token)

    updater.idle()

if __name__ == '__main__':
    main()