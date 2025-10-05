from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# --- Bot Configuration ---
TOKEN = "8212295363:AAFW-rCXssD1vPKyoMOMjvmj6HKansrNSHE"
MONETAG_LINK = "https://otieu.com/4/9976545"

WELCOME_MESSAGE = (
    "👋 Welcome to PocketMoney Bot!\n"
    "💸 Watch ads, click & start earning instantly.\n"
    "🚀 Start today and grow your income with us."
)

# --- Command Handler ---
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Start Earning 💰", url=MONETAG_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(WELCOME_MESSAGE, reply_markup=reply_markup)

# --- Main Function ---
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    print("🤖 PocketMoney Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
