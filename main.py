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
        [InlineKeyboardButton("📢 کانال‌های سیگنال ما", callback_data='signals_warning')]
    ]
    if update.message:
        await update.message.reply_text(
            "سلام! به ربات سیگنال خوش اومدی 🌟 لطفاً یکی از گزینه‌های زیر رو انتخاب کن:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            "سلام! به ربات سیگنال خوش اومدی 🌟 لطفاً یکی از گزینه‌های زیر رو انتخاب کن:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    try:
        if data == 'contact':
            keyboard = [
                [InlineKeyboardButton("📷 اینستاگرام", url='https://www.instagram.com/moamir_tradegroup')],
                [InlineKeyboardButton("🎮 دیسکورد", url='https://discord.gg/ZZBhyBhf')],
                [InlineKeyboardButton("🔙 بازگشت", callback_data='start')]
            ]
            await query.edit_message_text("📩 راه‌های ارتباط با ما:", reply_markup=InlineKeyboardMarkup(keyboard))

        elif data == 'signals_warning':
            keyboard = [
                [InlineKeyboardButton("✅ موافقم", callback_data='signals')],
                [InlineKeyboardButton("❌ مخالفم", callback_data='start')]
            ]
            await query.edit_message_text(
                """⚠️ شما باید در سیگنال‌ها، مدیریت سرمایه و ریسک منیجمنت را رعایت کنید.
اگر کال یا لیکویید شدید، ما هیچ مسئولیتی قبول نمی‌کنیم.""",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif data == 'signals':
            keyboard = [
                [InlineKeyboardButton("💱 سیگنال فارکس", callback_data='forex')],
                [InlineKeyboardButton("🪙 سیگنال کریپتو", callback_data='crypto')],
                [InlineKeyboardButton("🔙 بازگشت", callback_data='start')]
            ]
            await query.edit_message_text("📢 کانال‌های سیگنال ما:", reply_markup=InlineKeyboardMarkup(keyboard))

        elif data == 'forex':
            keyboard = [
                [InlineKeyboardButton("🎁 عضویت رایگان فارکس", callback_data='forex_free')],
                [InlineKeyboardButton("💎 عضویت VIP فارکس", callback_data='forex_vip')],
                [InlineKeyboardButton("🔙 بازگشت", callback_data='signals')]
            ]
            await query.edit_message_text("📊 انتخاب نوع عضویت در سیگنال فارکس:", reply_markup=InlineKeyboardMarkup(keyboard))

        elif data == 'crypto':
            keyboard = [
                [InlineKeyboardButton("🎁 عضویت رایگان کریپتو", callback_data='crypto_free')],
                [InlineKeyboardButton("💎 عضویت VIP کریپتو", callback_data='crypto_vip')],
                [InlineKeyboardButton("🔙 بازگشت", callback_data='signals')]
            ]
            await query.edit_message_text("📊 انتخاب نوع عضویت در سیگنال کریپتو:", reply_markup=InlineKeyboardMarkup(keyboard))

        elif data == 'crypto_vip':
            keyboard = [
                [InlineKeyboardButton("ثبت‌نام در Toobit", callback_data='toobit')],
                [InlineKeyboardButton("ثبت‌نام در LBank", callback_data='lbank')],
                [InlineKeyboardButton("🔙 بازگشت", callback_data='crypto')]
            ]
            await query.edit_message_text("صرافی مورد نظر رو انتخاب کن:", reply_markup=InlineKeyboardMarkup(keyboard))

        elif data == 'toobit':
            keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data='crypto_vip')]]
            await query.edit_message_text(
                "📌 ابتدا با این لینک در Toobit ثبت‌نام کن:\n"
                "https://www.toobit.com/\n"
                "کد رفرال: giWAS2\n\n"
                "✅ لطفاً ابتدا TXID (شناسه تراکنش) رو برای ما ارسال کن.\n"
                "بعد از تایید، UID خودتو بفرست تا به لیست VIP اضافه‌ت کنیم!",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif data == 'lbank':
            keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data='crypto_vip')]]
            await query.edit_message_text(
                "📌 ابتدا با این لینک در LBank ثبت‌نام کن:\n"
                "https://www.lbank.com/\n"
                "کد رفرال: به‌زودی اضافه میشه...\n\n"
                "✅ لطفاً ابتدا TXID (شناسه تراکنش) رو برای ما ارسال کن.\n"
                "بعد از تایید، UID خودتو بفرست تا به لیست VIP اضافه‌ت کنیم!",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif data == 'crypto_free':
            keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data='crypto')]]
            await query.edit_message_text(
                "🎁 برای عضویت رایگان:\n"
                "لطفاً ابتدا در یکی از صرافی‌های زیر با کد رفرال ما ثبت‌نام کن:\n\n"
                "🔗 Toobit: https://www.toobit.com/  (کد رفرال: giWAS2)\n"
                "🔗 LBank: https://www.lbank.com/\n\n"
                "سپس UID خودتو همینجا بفرست تا بررسی کنیم. اگه تایید شدی، با افتخار به کانال رایگان اضافه‌ت می‌کنیم!",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif data == 'forex_free':
            keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data='forex')]]
            await query.edit_message_text(
                "به‌زودی اطلاعات عضویت رایگان فارکس قرار می‌گیره.",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif data == 'forex_vip':
            keyboard = [[InlineKeyboardButton("🔙 بازگشت", callback_data='forex')]]
            await query.edit_message_text(
                "برای عضویت VIP فارکس لطفاً ابتدا پرداخت را از طریق لینک زرین‌پال انجام دهید.\n"
                "پس از پرداخت، ما با شما جهت عضویت در کانال VIP تماس می‌گیریم.",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        elif data == 'start':
            await start(update, context)

    except Exception as e:
        logger.error(f"خطا در button_handler: {e}")
        await query.edit_message_text("یه مشکلی پیش اومده. لطفاً دوباره امتحان کن.")

if __name__ == '__main__':
    keep_alive()
    print("✅ ربات روشن شد.")
    try:
        app = ApplicationBuilder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(button_handler))
        app.run_polling()
    except Exception as e:
        logger.error(f"❌ خطا در اجرای اصلی ربات: {e}")
