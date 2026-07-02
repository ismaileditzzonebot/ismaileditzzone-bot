import telebot
from telebot import types
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    open_btn = types.InlineKeyboardButton(
        "📂 Open XML",
        url="https://ismaileditzzone.blogspot.com/?m=1"
    )

    search_btn = types.InlineKeyboardButton(
        "🔍 Search XML",
        callback_data="search_xml"
    )

    markup.add(open_btn)
    markup.add(search_btn)

    bot.send_message(
        message.chat.id,
        "👋 Welcome to Ismail Editz Zone Bot\n\nSelect an option:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "search_xml")
def search(call):
    bot.send_message(call.message.chat.id, "📥 Enter XML Number:")
    bot.register_next_step_handler(call.message, find_xml)

def find_xml(message):
    number = message.text.strip()
    bot.send_message(
        message.chat.id,
        f"🔎 You searched for XML #{number}\n\nএই অংশে পরে Blogger পোস্টের লিংক দেখানো হবে।"
    )

print("Bot Running...")
bot.infinity_polling()
