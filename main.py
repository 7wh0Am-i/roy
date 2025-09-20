from telegram.ext import ApplicationBuilder, CommandHandler
from api.start import start
from api.get_num import get_num

# Enter your Telegram bot token here
TOKEN = "7597633089:AAEJEbapgoa7vNPH9bMzgrJK6Pn-TK4hQrk"

def main():
    """ Start the bot """
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers with proper formatting
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("num", get_num))

    app.run_polling()

if __name__ == '__main__':
    main()