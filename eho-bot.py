
 # python -m pip install requests
 # pip install pyTelegramBotAPI

# ехо бот

import telebot
bot = telebot.TeleBot('7723550221:AAHpiu_NBKfo2l0OgkZgjkaGpf5RTVqBPF4')

@bot.message_handler(content_types=['text'])
def mybot(message):
   bot.send_message(message.chat.id, message.text)
  
bot.polling(none_stop=True)


