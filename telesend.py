import telebot
import time

# Replace the values below with your bot token and the IDs of the source and target channels
TOKEN = '5326900387:AAEbeJRAdDEvXeY0OLKt3tWzn7hrdeV9Aq4'
SOURCE_CHANNEL_ID = -1001340803771
TARGET_CHANNEL_ID = -713506482

bot = telebot.TeleBot(TOKEN)

# Define a function to forward messages from the source channel to the target channel
@bot.message_handler(func=lambda message: message.chat.id == SOURCE_CHANNEL_ID)
def forward_message(message):
    bot.forward_message(chat_id=TARGET_CHANNEL_ID, from_chat_id=SOURCE_CHANNEL_ID, message_id=message.message_id)

# Start the bot
bot.polling()
