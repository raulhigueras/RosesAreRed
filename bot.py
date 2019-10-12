import telegram
from telegram.ext import (Updater, CommandHandler, MessageHandler, ConversationHandler)


ERROR_MESSAGE = 'Unexpected error.'
ERROR_NO_TEXT = 'Submmit a text, pls.'

def start(bot, update, user_data):
    reply_text = '''Try /help and start generating cool poems.'''
    bot.send_message(chat_id=update.message.chat_id, text=reply_text)


def help(bot, update):
    reply_text = '''
Only 1 command:
/poem - Ez pz you know what to do.
'''
    bot.send_message(chat_id=update.message.chat_id, text=reply_text)


def poem(bot, update, args, user_data):
    if len(args) == 0:
        bot.send_message(chat_id=update.message.chat_id, text=ERROR_NO_TEXT)
        return
    try:
        word = str(args[-1])
        reply_text = 'haha, ' + word
        bot.send_message(chat_id=update.message.chat_id, text=reply_text)
    except Exception as e:
        print(e)


def main():
    # Read token from file token.txt
    TOKEN = open('token.txt').read().strip()

    # Create the Updater and pass it your bot's token
    updater = Updater(token=TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', start, pass_user_data=True))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('poem', poem, pass_args=True, pass_user_data=True))
    # Start the Bot
    updater.start_polling()


if __name__ == '__main__':
    main()
