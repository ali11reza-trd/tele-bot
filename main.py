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
            [InlineKeyboardButton("🎁 عضویت رایگان کریپتو", callback_data='crypto_free')],
            [InlineKeyboardButton("💎 عضویت VIP کریپتو", callback_data='crypto_vip')],
            [InlineKeyboardButton("🔙 بازگشت", callback_data='signals')]
        ]
        await query.edit_message_text("📊 انتخاب نوع عضویت در سیگنال کریپتو:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'crypto_vip':
        keyboard = [
            [InlineKeyboardButton("ثبت‌نام در Toobit", callback_data='toobit')],
            [InlineKeyboardButton("ثبت‌نام در LBank", callback_data='lbank')],
            [InlineKeyboardButton("🔙 بازگشت", callback_data='crypto')]
        ]
        await query.edit_message_text("صرافی مورد نظر رو انتخاب کن:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == 'toobit':
        await query.edit_message_text("""📌 ابتدا با این لینک در Toobit ثبت‌نام کن:
https://www.toobit.com/
کد رفرال: giWAS2

✅ پس از ثبت‌نام، لطفاً UID خود را ارسال کنید تا بررسی و افزودن به لیست VIP انجام شود.""")

    elif query.data == 'lbank':
        await query.edit_message_text("""📌 ابتدا با این لینک در LBank ثبت‌نام کن:
https://www.lbank.com/
کد رفرال: به‌زودی اضافه می‌شود...

✅ پس از ثبت‌نام، لطفاً UID خود را ارسال کنید تا بررسی انجام شود.""")

    elif query.data == 'crypto_free':
        await query.edit_message_text("""🎁 برای دریافت سیگنال رایگان:
ابتدا در صرافی زیر ثبت‌نام کن:

🔗 https://www.toobit.com/
کد رفرال: giWAS2

سپس UID خود را ارسال کن. پس از تأیید، لینک عضویت برات فرستاده میشه.
(به‌زودی بررسی UID از طریق API انجام خواهد شد.)""")

    elif query.data == 'start':
        await start(update, context)

if __name__ == '__main__':
    keep_alive()
    print("✅ ربات روشن شد.")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.run_polling()
