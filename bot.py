from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from telegram.error import BadRequest

TOKEN = "8772785235:AAFm9B3oOPgY6N05k1MKqjNTc9Aa1e9JfH0"

async def hide_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Update received")

    if update.message and update.message.new_chat_members:
        print("Join detected!")
        try:
            await update.message.delete()
            print("Deleted join message")
        except BadRequest as e:
            print("Error:", e)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, hide_join))

   
 print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
    async def hide_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
     if update.message and update.message.new_chat_members:
        try:
            await update.message.delete()
        except:
            pass
async def welcome_new_members(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.new_chat_members:
        for user in update.message.new_chat_members:
            try:
                # Delete the default join message
                await update.message.delete()
            except:
                pass

            # Send custom welcome message
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"👑 Welcome {user.first_name} to My Kingdom.\n\nThis is King Abel Room — enjoy your time and feel free."
            )
def main():
    app = Application.builder().token(TOKEN).build()

    # 👇 handler goes HERE
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_members))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
