from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import logging
from keep_alive import keep_alive
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📞 ارتباط با ما", callback_data='contact')],
        [InlineKeyboardButton("📢 کانال‌های سیگنال ما", callback_data='signals')]
    ]
    await update.message.reply_text(
        "سلام! به ربات سیگنال خوش اومدی 🌟 لطفاً یکی از گزینه‌های زیر رو انتخاب کن:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'contact':
        keyboard = [
            [InlineKeyboardButton("📷 اینستاگرام", url='https://www.instagram.com/moamir_tradegroup')],
            [InlineKeyboardButton("🎮 دیسکورد", url='https://discord.gg/ZZBhyBhf')],
            [InlineKeyboardButton("🛠 پشتیبانی", url='https://t.me/YOUR_SUPPORT')],
            [InlineKeyboardButton("🔙 بازگشت", callback_data='start')]
        ]
        await query.edit_message_text("📩 راه‌های ارتباط با ما:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'signals':
        keyboard = [
            [InlineKeyboardButton("💱 سیگنال فارکس", callback_data='forex')],
            [InlineKeyboardButton("🪙 سیگنال کریپتو", callback_data='crypto')],
            [InlineKeyboardButton("🔙 بازگشت", callback_data='start')]
        ]
        await query.edit_message_text("📢 کانال‌های سیگنال ما:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'forex':
        keyboard = [
            [InlineKeyboardButton("🎁 عضویت رایگان فارکس", callback_data='forex_free')],
            [InlineKeyboardButton("💎 عضویت VIP فارکس", callback_data='forex_vip')],
            [InlineKeyboardButton("🔙 بازگشت", callback_data='signals')]
        ]
        await query.edit_message_text("📊 انتخاب نوع عضویت در سیگنال فارکس:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'crypto':
        keyboard = [
            [InlineKeyboardButton("🎁 عضویت رایگان کریپتو", url="https://t.me/+Ab2sDDf9WCQ4NWFk")],
            [InlineKeyboardButton("💎 عضویت VIP کریپتو", callback_data='crypto_vip')],
            [InlineKeyboardButton("🔙 بازگشت", callback_data='signals')]
        ]
        await query.edit_message_text("📊 انتخاب نوع عضویت در سیگنال کریپتو:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'crypto_vip':
        text = (
            "ابتدا با یکی از صرافی‌های زیر ثبت‌نام کن:

"
            "1️⃣ Toobit:
"
            "🔗 لینک ثبت‌نام: https://www.toobit.com/
"
            "💬 کد رفرال: giWAS2

"
            "⏳ پس از ثبت‌نام، UID خود را ارسال کنید تا عضویت VIP شما بررسی شود."
        )
        await query.edit_message_text(text)

    elif query.data == 'start':
        await start(update, context)

if __name__ == '__main__':
    keep_alive()
    print("✅ ربات روشن شد.")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()