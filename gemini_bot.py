# Bot with message handler
from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import requests 

token = "7208364543:AAGNFaoSx4ODC08706PvrQt_8b0SQi_5_50"
gen_ai_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
param = {
    "key" : "AIzaSyDUsUJUaoGcmJgxT92zpi_yJDn0ZVO0iO8"
}

def json_creator(prompt):
    json_file = {
  "contents": [
    {
      "parts": [
        {
          "text": prompt
        }
      ]
    }
  ]
}
    return json_file

# Command handler for /start 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text("Salom men rasm generatsiya qiluvchi AI man.")

# Command handler for /help command
async def help_command(update : Update, context : ContextTypes):
    await update.message.reply_text("Mavjud bot komandalari : /start, /help")

# Command handler for /about_me
async def about_me(update : Update, context : ContextTypes):
    await update.message.reply_text("я джемени чат бот")

# Message handler
async def message_handler(update : Update, context : ContextTypes) :
    user_text = update.message.text 
    js_send = json_creator(user_text)
    res = requests.post(url = gen_ai_url, params = param, json = js_send).json()
    final_res = res['candidates'][0]['content']['parts'][0]['text']

    await update.message.reply_text(final_res)

if __name__ == '__main__':
    app = ApplicationBuilder().token(token = token).build()
    
    # Handlers
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about_me", about_me))

    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    app.run_polling()