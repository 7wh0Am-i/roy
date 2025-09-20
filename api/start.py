from telegram.ext import ContextTypes

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    """ Display welcome message for the /start command """
    await update.message.reply_text(
        "👋 Welcome to TESTING OSINT Helper Bot\n"
        "🙏 I can help you find information using various search commands.\n"
        "📌 Available Commands:\n"
        "/num - Finds details linked to a 10-digit number.\n"
        "✨ Stay safe and respect privacy!\n",
        parse_mode='Markdown'
    )