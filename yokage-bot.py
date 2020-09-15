from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
bot_token= '986055221:AAG1flK7EZZxzWIZrWmHqnv29oWLDxcge10'

updater = Updater(token= bot_token, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Olá, eu sou o NA BOT, Bem vindo!!, Esse é o nosso discord: https://discord.gg/QN8Tr4E")
 
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
updater.start_polling()