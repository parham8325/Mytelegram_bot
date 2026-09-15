import os
import telebot

# توکن ربات رو از یه جای امن (متغیر محیطی) می‌خونیم، نه اینکه توی کد بنویسیمش
BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

# وقتی کسی دستور /start رو بزنه، این پیام رو جواب میده
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! 👋 من یه ربات ساده‌ام. هرچی بنویسی رو برات تکرار می‌کنم.")

# هر پیام دیگه‌ای که بفرستی رو عینا تکرار می‌کنه (echo)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# ربات رو روشن نگه می‌داره و منتظر پیام‌های تلگرام می‌مونه
bot.infinity_polling()
