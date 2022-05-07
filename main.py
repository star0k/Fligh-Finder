API_KEY = "5251282624:AAFvFD7NJJuiAbZiFfbuBG9CIxY5tVq6s2g"
from telegram.ext import *

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update



def start_command (update , context) :
    update.message.reply_text("Send me any number with country region (+xx)")

def handle_message(update : Update , context:CallbackContext):
    text = str(update.message.text).lower()
    if numCheck(str(text) , update) :
        response = f"https://api.whatsapp.com/send?phone={text}"
        keyboard = [InlineKeyboardButton("Start Chat", callback_data='1'),]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    query.edit_message_text(text=f"Selected option: {query.data}")



def main ():
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.text,handle_message))


    updater.start_polling()
    updater.idle()

main()