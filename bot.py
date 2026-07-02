import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = os.getenv("CHANNEL_USERNAME")

async def check_join(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    if await check_join(context.bot, user.id):
        await update.message.reply_text(
            f"🎉 Welcome {user.first_name}!\n\n✅ Verification Successful.\n\nROYAL X ARENA ❤️"
        )
        return

    buttons = [
        [InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL.replace('@','')}")],
        [InlineKeyboardButton("✅ Verify", callback_data="verify")]
    ]

    await update.message.reply_text(
        "⚠️ Pehle channel join karo.\n\nJoin karne ke baad Verify button dabao.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
