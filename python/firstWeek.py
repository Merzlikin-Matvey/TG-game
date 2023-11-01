import telebot
import os
from dotenv import load_dotenv
import time

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

def startWeek1(message):
    bot.register_next_step_handler(message, f1)



def f1(message):
    bot.send_message(message.chat.id, '8:50. 229 кабинет, алгебра')
    time.sleep(1.5)
    
    keyboard = telebot.types.ReplyKeyboardMarkup()
    key_yes = telebot.types.KeyboardButton(text="Да, делал")
    key_probably = telebot.types.KeyboardButton(text="Возможно частично")
    key_no = telebot.types.KeyboardButton(text="Нет, я не успел")

    keyboard.add(key_yes, key_probably, key_no)
    bot.send_message(message.chat.id, 'Иван: Ты домашку делал?', reply_markup=keyboard)                                                                                                                               
    bot.register_next_step_handler(message, f2)

def f2(message):
    print(message.text)
    bot.send_message(message.chat.id, 'я здеся')
    if message.text == "Да, делал":
        bot.send_message(message.chat.id, "Иван: Отлично, просто я не успел. Прикрой меня")
        time.sleep(1)
        bot.send_message(message.chat.id, "10 минут спустя")
        time.sleep(1)
        bot.send_message(message.chat.id, "Дмитрий Евгеньевич: Так, кто сделал домашку?")
        
        keyboard = telebot.types.InlineKeyboardMarkup()
        key_queit = telebot.types.InlineKeyboardButton(text="Промолчу..", callback_data="/Промолчу")
        key_say = telebot.types.InlineKeyboardButton(text="Я отвечу, зачем молчать?", callback_data="/Скажу")
    else:
        bot.send_message(message.chat.id, message.text)
