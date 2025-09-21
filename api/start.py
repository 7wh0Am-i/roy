from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode   # ✅ this was missing
from telegram.ext import ContextTypes
from telegram.error import BadRequest

# Replace with your channel/group usernames
REQUIRED_CHANNELS = ["@loottoon","@Roy_726i"]

async def check_membership(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Check if the user is a member of required channels/groups"""
    user_id = update.effective_user.id
    bot = context.bot

    for chat in REQUIRED_CHANNELS:
        try:
            member = await bot.get_chat_member(chat, user_id)
            if member.status in ("left", "kicked"):
                return False
        except BadRequest:
            return False
    return True


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command with force join + welcome message"""

    if not await check_membership(update, context):
        keyboard = [
            [
                InlineKeyboardButton("📌 Join Group", url="https://t.me/loottoon"),
                InlineKeyboardButton("📢 Join Channel", url="https://t.me/Roy_726i"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "⚠️ To use this bot, you must join our group and channel first.",
            reply_markup=reply_markup
        )
        return

    # ✅ If user is a member, show your welcome message
    await update.message.reply_text(
        "👋 Welcome to <b>TESTING OSINT Helper Bot</b>\n\n"
        "🙏 I can help you find information using various search commands.\n\n"
        "📌 <b>Available Commands:</b>\n"
        "/num - Finds details linked to a 10-digit number.\n\n"
        "✨ Stay safe and respect privacy!\n\n"
        "👤 Owner: <a href='https://t.me/Roy_726'>@Roy_726</a>",
        parse_mode=ParseMode.HTML
    )
