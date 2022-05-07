
"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://git.io/JOmFw.
"""
import logging
Number =  ""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, bot
from telegram.ext import  *
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
CHAT_ID = ""
updater : Update

msgentrymode = False
def numCheck (stri , update) :
    global  Number
    z = 0
    for num in stri:
        if z == 0:
            if num != "+":
                update.message.reply_text("You need to add country code first")
                return False
            else:
                z += 1
        else:
           try :
                 nuk = int(num)
                 z += 1
           except :
               update.message.reply_text("Only enter numbers !")
               return False
    Number = stri
    return True


def msghandler (update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    global CHAT_ID
    CHAT_ID  = update.message.chat_id
    print(msgentrymode)
    if msgentrymode :
        keyboard = [
            [
                InlineKeyboardButton(text="Open Chat", callback_data='1',
                                     url=f"https://api.whatsapp.com/send?phone={Number}&text={update.message.text}"),
            ]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(f'Number : {Number} \n Message : \n{update.message.text}', reply_markup=reply_markup)

    else:
        text = str(update.message.text).lower()
        if numCheck(str(text), update):
            keyboard = [
                [
                    InlineKeyboardButton(text="Open Chat", callback_data='1' ,  url=f"https://api.whatsapp.com/send?phone={text}") ,
                    InlineKeyboardButton(text="specify message", callback_data='2')

            ]]

            reply_markup = InlineKeyboardMarkup(keyboard)

            update.message.reply_text(f'Number : {text}', reply_markup=reply_markup)

def start(update: Update, context: CallbackContext) -> None:


    update.message.reply_text('Send me any number with country region (+xx)')


def replyan (update :Update , context) :
   print(update.message.text)

def afterask () :
    global msgentrymode
    global CHAT_ID
    mybot = bot.Bot("5251282624:AAFvFD7NJJuiAbZiFfbuBG9CIxY5tVq6s2g")
    mybot.send_message(chat_id = CHAT_ID , text = "Enter your message")
    msgentrymode = True


def button(update: Update, context: CallbackContext ) -> None:
    """Parses the CallbackQuery and updates the message text."""
    global updater
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    print (query.data)
    if query.data == "2" :
        afterask()

def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")



def get_chat_id( message):
    if message.chat.type == 'private':
        return message.user.id
    return message.chat.id
def main() -> None:
    """Run the bot."""
    global updater
    # Create the Updater and pass it your bot's token.
    updater = Updater("5251282624:AAFvFD7NJJuiAbZiFfbuBG9CIxY5tVq6s2g")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text,msghandler))


    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
