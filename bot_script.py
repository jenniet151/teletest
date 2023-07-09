from telegram.ext import Updater, MessageHandler, filters

# Function to handle incoming messages
def handle_message(update, context):
    message = update.message.text

    
    # Check if the message format matches the required pattern
    if message.startswith('⚜️ᴄᴀʀᴅ -»') and '|' in message:
        # Extract the relevant portion of the message
        text = message.split('-» ')[1]

        # Forward the modified message to the target group
        context.bot.send_message(chat_id='TARGET_GROUP_ID', text='/chk ' + text)

# Create an instance of the Updater and pass your bot token
updater = Updater(secret_token='YOUR_BOT_TOKEN', use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the message handler
dispatcher.add_handler(MessageHandler(Filters.text & (Filters.chat('CHANNEL_A_ID') | Filters.group('GROUP_A_ID')), handle_message))

# Start the bot
updater.start_polling()
