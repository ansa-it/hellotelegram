import sys
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Logging konfigurieren (optional, für Debugging)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start Befehl-Handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello World from Telegram")

def main():
    if len(sys.argv) != 2:
        print("Usage: python telegram_bot.py <YOUR_BOT_TOKEN>")
        sys.exit(1)

    bot_token = sys.argv[1]

    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == '__main__':
    main()
