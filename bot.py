from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram.error import BadRequest
import os

TOKEN = os.getenv("8772785235:AAHG_WGdC1JVAmwU-ZJtrD63zpIASk6F43w")  # safer for Railway

# ✅ Welcome + delete join message
async def welcome_new_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.new_chat_members:
        for user in update.message.new_chat_members:
            try:
                # Delete default join message
                await update.message.delete()
            except BadRequest:
                pass

            # Send welcome message
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"👑 Welcome {user.first_name} to My Kingdom.\n\nThis is King Abel Room — enjoy your time and feel free."
            )

def main():
    app = Application.builder().token(TOKEN).build()

    # ✅ ONLY ONE handler
    app.add_handler(
        MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_members)
    )

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()