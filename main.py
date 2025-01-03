#Этот скрипт сделан AngelKlear

import telebot
from telebot import types



bot = telebot.TeleBot('8101018755:AAEtKbqUAP4y99vczrHg7HruLLn5pkZHq3c')



@bot.message_handler(commands=['start'])
def main(message):
 
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('AngelKlear')
    btn2 = types.KeyboardButton('Kaylopeer')
    markup.add(btn1, btn2)

 
  

    
 
 
    bot.send_message(message.chat.id, f'Приветсивую тебя <b><u>{message.from_user.first_name}</u></b>, меня зовут <b><u>VidechKA</u></b> или же <b><u>@videchKAbot</u></b>', parse_mode='html')
    bot.send_message(message.chat.id, 'Выберите автора!', reply_markup=markup)
    
@bot.message_handler(commands=['info'])
def info(message):
       markup = types.ReplyKeyboardMarkup()
       btn1 = types.KeyboardButton('AngelKlear')
       btn2 = types.KeyboardButton('Kaylopeer')
       markup.add(btn1, btn2)
       
       
       
       bot.send_message(message.chat.id, f'<b><u>{message.from_user.first_name}</u></b>, вот информация обо мне:\n -------------------------------\n Я бот который создан на Python 3.13\n Был создан на библиотеки pyTelegramBotAPI (или же TeleBot)\n -------------------------------\n Авторы:\n -------------------------------\n @KAYLOPEER - Дизайнер\n @AngelKlear - Скриптер\n -------------------------------', reply_markup=markup, parse_mode="html")
       
       bot.send_message(message.chat.id, 'Выберите автора!', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def func(message):
 if(message.text == 'AngelKlear'):
        bot.send_message(message.chat.id, 'Вы выбрали AngelKlear')
        bot.send_message(message.chat.id, '👇 Все видео от AngelKlear там 👇')
        bot.send_message(message.chat.id, 'https://t.me/+-HbKXVBss3kxZWEy')
        
        
 elif(message.text == 'Kaylopeer'):
       bot.send_message(message.chat.id, 'Вы выбрали Kaylopeer')
       bot.send_message(message.chat.id, '👇 Все видео от Kaylopeer там 👇')
       bot.send_message(message.chat.id, 'https://t.me/+2-vEbcvvCYw4NjIy')
        
 
 
 
 
bot.polling(none_stop=True)