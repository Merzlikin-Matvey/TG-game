import time
import telebot
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

player_name = None
player_class = None


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    send = ('Привет! В этой игре тебе нужно будет дожить до сессии, а потом успешно сдать ее! '
            'Ты будешь играть за одного из выбранных персонажей. У каждого из них свои начальные характеристики. '
            'Каждый раз у тебя будет выбор, от которого зависит '
            'дальнейшее развитие событий')
    bot.send_message(chat_id, send)
    time.sleep(2)
    bot.send_message(chat_id, "Введи свое имя")
    bot.register_next_step_handler(message, get_name)



def get_name(message):
    global player_name
    player_name = message.text

    keyboard = telebot.types.ReplyKeyboardMarkup()
    key_botan = telebot.types.KeyboardButton(text='Ботан')
    key_sportsman = telebot.types.KeyboardButton(text='Спортсмен')
    key_poet = telebot.types.KeyboardButton(text='Поэт')
    key_person = telebot.types.KeyboardButton(text='Человек')
    keyboard.add(key_botan, key_sportsman, key_poet, key_person)

    bot.send_message(message.chat.id, 'Теперь выбери, за какой класс хочешь играть', reply_markup=keyboard)
    bot.register_next_step_handler(message, get_class)



def get_class(message):
    global player_class, player_name
    player_class = message.text

    send = f'{player_name}, {player_class.lower()} это отличный выбор!'
    bot.send_message(message.chat.id, send)
    time.sleep(1)

    keyboard = telebot.types.ReplyKeyboardMarkup()
    keys = []
    for i in range(1, 6 + 1):
        keys.append(telebot.types.KeyboardButton(text=str(i)))

    keyboard.add(*keys)
    bot.send_message(message.chat.id, 'Определись, в какой группе по математике будешь учиться', reply_markup=keyboard)
    bot.register_next_step_handler(message, get_group)


def get_group(message):
    if message.text == '1':
        bot.send_message(message.chat.id, 'Первая группа. А других вариантов и быть не могло!')
    elif message.text in list(map(str, [i for i in range(2, 6 + 1)])):
        bot.send_message(message.chat.id, 'Фатальная ошибка. Вы проиграли')







if __name__ == '__main__':
    bot.polling(True)