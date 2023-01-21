import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters
bot = telegram.Bot(token="5849944821:AAHpqts-UpWJDgiItTVqjjPvIFgIf0JcK5M")
updater = Updater(token="5849944821:AAHpqts-UpWJDgiItTVqjjPvIFgIf0JcK5M", use_context=True)


initial_keyboard = [[InlineKeyboardButton("IT", callback_data="1"),
                    InlineKeyboardButton("CS", callback_data="2")],
                    [InlineKeyboardButton("EC", callback_data="3"),
                    InlineKeyboardButton("EESE", callback_data="4")],
                    [InlineKeyboardButton("MECH", callback_data="5"),
                    InlineKeyboardButton("CIVIL", callback_data="6")]
                    ]

initial_reply_markup = InlineKeyboardMarkup(initial_keyboard)

# Send the message with the initial keyboard
bot.send_message(chat_id="998636772", text="Select your department", reply_markup=initial_reply_markup)

# Function to handle the callback query
def handle_callback_query(update, context):
    query = update.callback_query
    data = query.data

    # Create the new keyboard based on the callback data
    if data == "1":
        new_keyboard = [[InlineKeyboardButton("1st", callback_data="s1"),
                         InlineKeyboardButton("2nd", callback_data="s2")],
                        [InlineKeyboardButton("3rd", callback_data="s3"),
                         InlineKeyboardButton("4th", callback_data="s4")],
                        [InlineKeyboardButton("5th", callback_data="s5"),
                         InlineKeyboardButton("6th", callback_data="s6")],
                        [InlineKeyboardButton("7th", callback_data="s7"),
                         InlineKeyboardButton("8th", callback_data="s8")]]
        new_reply_markup = InlineKeyboardMarkup(new_keyboard)
        bot.edit_message_text(chat_id=query.message.chat_id,
                              message_id=query.message.message_id,
                              text="Choose your Semester",
                              reply_markup=new_reply_markup)
    else:
        bot.answer_callback_query(query.id, text="Invalid selection.")

# Create an Updater
from telegram.ext import Updater
updater = Updater(token="5849944821:AAHpqts-UpWJDgiItTVqjjPvIFgIf0JcK5M")

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Add a handler for callback queries
from telegram.ext import CallbackQueryHandler
dp.add_handler(CallbackQueryHandler(handle_callback_query))

# Start the bot
updater.start_polling()

updater.idle()