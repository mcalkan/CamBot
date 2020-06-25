import telebot
import time
from datetime import datetime
import datetime
import array


bot_token ='token'
bot =telebot.TeleBot(token=bot_token)

an = datetime.datetime.now()
tarih = datetime.datetime.ctime(an)

kisiler = ["hak", "hukuk", "adalet"]

for i in range(len(personal)):
    @bot.message_handler(commands=kisiler[i])
    def send_welcome(message):
        bot.reply_to(message,'Login:tarih)


@bot.message_handler(commands=personal[0])
def send_welcome(message):
    bot.reply_to(message, personal[0]+ ': Login + tarih)

@bot.message_handler(commands=personal[1])
def send_welcome1(message1):
    bot.reply_to(message1, 'test message
    
@bot.message_handler(commands=personal[2])
def send_welcome2(message2):
    bot.reply_to(message2, 'Bos )

bot.polling()
