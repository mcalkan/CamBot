import telebot
import time
from datetime import datetime
import datetime
import array


bot_token ='964279669:AAEYDJUP0E6dWroXd01Uq6shqpClggNc-z0'
bot =telebot.TeleBot(token=bot_token)

an = datetime.datetime.now()
tarih = datetime.datetime.ctime(an)

kisiler = ["Hazal", "yetis", "mustafa"]

#for i in range(len(kisiler)):
 #   @bot.message_handler(commands=kisiler[i])
  #  def send_welcome(message):
   #     bot.reply_to(message,'Giris Saati: ' + tarih)


@bot.message_handler(commands=kisiler[0])
def send_welcome(message):
    bot.reply_to(message, kisiler[0]+ ': Giris Saati: ' + tarih)

#@bot.message_handler(commands=kisiler[1])
#def send_welcome1(message1):
#    bot.reply_to(message1, 'Adnan Hep Bırçi')
#    
#@bot.message_handler(commands=kisiler[2])
#def send_welcome2(message2):
#    bot.reply_to(message2, 'Patron Geldi')

bot.polling()
