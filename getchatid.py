import telegram

bot = telegram.Bot(token="5632461012:AAFtcNjKdHz2fFk_QAnukYh13TVA1iDBg1g")

# Get the latest update from the user
updates = bot.get_updates()
if updates:
    update = updates[-1]
    # Extract the chat ID
    chat_id = update.message.chat_id
    # Print the chat ID
    print(chat_id)
else:
    print("No updates received yet.")
