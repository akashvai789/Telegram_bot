# প্রয়োজনীয় লাইব্রেরি ইমপোর্ট করি
from telegram.ext import Updater, CommandHandler

# 👉 এখানে BotFather থেকে পাওয়া টোকেনটি বসাও
BOT_TOKEN = "7532406971:AAFAKnKQ3mS00UUSy-beb1LhHGTIDA0l65E"

# /start কমান্ডে যেটা ঘটবে
def start(update, context):
    update.message.reply_text("হ্যালো! আমি আপনার তৈরি করা টেলিগ্রাম বট 🤖")

# বট চালানোর মূল ফাংশন
def main():
    # বট সেটআপ
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # /start কমান্ড হ্যান্ডলারে যুক্ত করা
    dp.add_handler(CommandHandler("start", start))

    # বট চালু করা
    updater.start_polling()
    print("✅ Bot চলছে... Telegram-এ গিয়ে /start টাইপ করে দেখুন!")
    updater.idle()

# প্রোগ্রাম চালু করার এন্ট্রি পয়েন্ট
if __name__ == '__main__':
    main()
