import telebot
import time

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🤖 أهلاً بك في نظام البوت السيبراني التجريبي.\nأرسل /status أو /bruteforce <هدف>")

@bot.message_handler(commands=['status'])
def check_status(message):
    bot.reply_to(message, "🟢 النظام يعمل بنجاح ومتصل عبر Render.")

@bot.message_handler(commands=['bruteforce'])
def handle_bruteforce(message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        bot.reply_to(message, "⚠️ يرجى تحديد الهدف، هكذا:\n`/bruteforce <target>`", parse_mode="Markdown")
        return
    target = parts[1]
    bot.reply_to(message, f"🔍 جاري الفحص التجريبي للهدف: `{target}`...", parse_mode="Markdown")
    time.sleep(2)
    bot.reply_to(message, f"📊 اكتمل الفحص بنجاح للهدف: `{target}`", parse_mode="Markdown")

print("Cyber Bot is active and listening for commands...")
bot.infinity_polling()
