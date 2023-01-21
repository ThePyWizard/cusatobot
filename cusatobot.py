import os
import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Set up Telegram bot
bot = telegram.Bot(token="5849944821:AAHpqts-UpWJDgiItTVqjjPvIFgIf0JcK5M")
updater = Updater(token="5849944821:AAHpqts-UpWJDgiItTVqjjPvIFgIf0JcK5M", use_context=True)
dispatcher = updater.dispatcher

# Define a function to handle incoming files
def forward_file(update, context):
    file_id = update.message.document.file_id
    file = bot.get_file(file_id)
    user_id = update.message.from_user.id
    # Forward the file to the user
    bot.send_document(chat_id=user_id, document=file)

# Add the message handler to the dispatcher
file_handler = MessageHandler(Filters.document, forward_file)
dispatcher.add_handler(file_handler)
#hi i am jishnu
# Start the bot
updater.start_polling()
updater.idle()
