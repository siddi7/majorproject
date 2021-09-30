from telegram.ext import Updater, MessageHandler, Filters
from Adafruit_IO import Client

import os

client_name=os.getenv('client_name')
client_api=os.getenv('client_api')

aio=Client(client_name,client_api)

def light_on(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Lights on !')
  aio.send('light',1)

def light_off(bot,update):
   chat_id = bot.message.chat_id
   bot.message.reply_text('  Lights off ')
   aio.send('light',0) 

def fan_on(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan ON')
  aio.send('fan',1) 

def fan_off(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan OFF')
  aio.send('fan',0)

def main(bot,update):
  a= bot.message.text
  if a =="turn on the lights":
    light_on(bot,update)

  if a=="turn off the lights":
    light_off(bot,update)

  if a=="turn on the fan":
    fan_on(bot,update)

  if a=="turn off the fan":
    fan_off(bot,update)

bot_token =os.getenv('bot_token')
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
