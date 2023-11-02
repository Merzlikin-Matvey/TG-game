'''
Я всю игру сделал в одном файле так как не смог адекватно разделить это на файлы
Проблема с bot.register_next_step_handler
Если найдется человек, который сможет мне помочь, буду благодарен ☺
'''

import time
import os

from dotenv import load_dotenv
import telebot
import numpy as np

from player import Player

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

player_name = 'Аллллллексей'
player_class = 'Ботан'
player = Player('Аллллллексей', 'Ботан')


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
    global player, player_name, player_class
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
    global player, player_name, player_class
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
    global player, player_name, player_class
    player = Player(player_name, player_class)
    if message.text == '1':
        bot.send_message(message.chat.id,
                         'Первая группа. А других вариантов и быть не могло!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        f_1(message)
    elif message.text in list(map(str, [i for i in range(2, 6 + 1)])):
        bot.send_message(message.chat.id, 'Фатальная ошибка. Вы проиграли',
                         reply_markup=telebot.types.ReplyKeyboardRemove())


def f_1(message):
    time.sleep(1)
    bot.send_message(message.chat.id, "День 1")
    time.sleep(1)
    bot.send_message(message.chat.id, '8:50. 229 кабинет, алгебра')
    time.sleep(1.5)

    keyboard = telebot.types.ReplyKeyboardMarkup()
    key_yes = telebot.types.KeyboardButton(text="Да, делал")
    key_probably = telebot.types.KeyboardButton(text="Возможно частично")
    key_no = telebot.types.KeyboardButton(text="Нет, я не успел")

    keyboard.add(key_yes, key_probably, key_no)
    bot.send_message(message.chat.id, 'Иван: Ты домашку делал?', reply_markup=keyboard)
    bot.register_next_step_handler(message, f_2)

def alex(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    key_yes = telebot.types.KeyboardButton(text="Да, пойду")
    key_probably = telebot.types.KeyboardButton(text="Нет, я устал, пойду домой")
    keyboard.add(key_yes, key_probably)

    bot.send_message(message.chat.id, "Алексей: Ты пойдешь на литературу?", reply_markup=keyboard)

    bot.register_next_step_handler(message, f_3)

def f_2(message):
    if message.text == "Да, делал":
        bot.send_message(message.chat.id, "Иван: Отлично, просто я не успел. Прикрой меня",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        time.sleep(1)
        bot.send_message(message.chat.id, "10 минут спустя")
        time.sleep(1)

        keyboard = telebot.types.InlineKeyboardMarkup()
        key_quiet = telebot.types.InlineKeyboardButton(text="Промолчу..", callback_data="/Промолчу")
        key_say = telebot.types.InlineKeyboardButton(text="Я отвечу, зачем молчать?", callback_data="/Скажу")

        keyboard.add(key_quiet, key_say)
        bot.send_message(message.chat.id, "Дмитрий Евгеньевич: Так, кто сделал домашку?", reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def handle_callback_query(call):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Дмитрий Евгеньевич: Так, кто сделал домашку?", reply_markup=None)

            if call.data == '/Промолчу':
                time.sleep(2)
                bot.send_message(call.message.chat.id, "Дмитрий Евгеньевич: Лес рук...")
                time.sleep(1)
                bot.send_message(call.message.chat.id, "Дмитрий Евгеньевич: Тогда пойдем по списку")
                time.sleep(1)
                bot.send_message(call.message.chat.id, "Дмитрий Евгеньевич: К доске пойдет..")
                time.sleep(1)
                bot.send_message(call.message.chat.id, "Дмитрий Евгеньевич: К доске пойдет...")
                time.sleep(1)
                bot.send_message(call.message.chat.id, "Дмитрий Евгеньевич: К доске пойдет....")

                loser = np.random.choice(np.array(
                    [player.player_name, player.player_name, "Иван"]))
                bot.send_message(call.message.chat.id, loser)

                if loser == player.player_name:
                    time.sleep(1)
                    bot.send_message(call.message.chat.id,
                                     f' Дмитрий Евгеньевич:{player.player_name}, решите это уравнение')
                    photo = open('../img/cubic_equation.jpg', 'rb')
                    bot.send_photo(call.message.chat.id, photo=photo)

                    def f_2_1(message):
                        try:
                            ans = sorted(list(map(int, message.text.split())))
                        except:
                            ans = -1
                        if ans == [57, 58, 239]:
                            bot.send_message(message.chat.id, "Дмитрий Евгеньевич: Фантастика! Верно!")
                            time.sleep(1)
                            bot.send_message(message.chat.id, player.intelligence(5))
                            player.rep(10)
                            bot.send_message(message.chat.id, "Через час")
                            time.sleep(2)
                            alex(message)
                        else:
                            bot.send_message(message.chat.id, 'Дмитрий Евгеньевич: Неправильно! Садитесь, 2!')
                            bot.send_message(message.chat.id, player.intelligence(-5))
                            player.rep(-10)
                            time.sleep(2)
                            bot.send_message(message.chat.id, "Дмитрий Евгеньевич: Иван, а вы сделали этот номер?")
                            time.sleep(2)
                            bot.send_message(message.chat.id, "Иван: Нет, я не успел")
                            time.sleep(2)
                            bot.send_message(message.chat.id, "Дмитрий Евгеньевич: не успевают только неуспевающие!")
                            time.sleep(2)
                            bot.send_message(message.chat.id, "Через час")
                            time.sleep(2)

                            keyboard = telebot.types.ReplyKeyboardMarkup()
                            key_sorry = telebot.types.KeyboardButton(text="Прости, ошибся")
                            key_lol = telebot.types.KeyboardButton(text="Я пошутил :D")
                            keyboard.add(key_sorry, key_lol)

                            bot.send_message(message.chat.id,
                                             f"Иван: Блин, {player.player_name}, ты же сказал что сделал домашку",
                                             reply_markup=keyboard)

                            def f_2_1_1(message):
                                if message.text == "Прости, ошибся":
                                    bot.send_message(message.chat.id, "Иван: Да ладно, бывает",
                                                     reply_markup=telebot.types.ReplyKeyboardRemove())
                                else:
                                    bot.send_message(message.chat.id, "Иван: Друг, называется",
                                                     reply_markup=telebot.types.ReplyKeyboardRemove())

                                alex(message)

                            bot.register_next_step_handler(message, f_2_1_1)

                    bot.register_next_step_handler(message, f_2_1)

                else:
                    bot.send_message(message.chat.id, "Иван: Я не успел сделать домашку")
                    time.sleep(2)
                    bot.send_message(message.chat.id, "Дмитрий Евгеньевич: не успевают только неуспевающие!")
                    time.sleep(2)
                    bot.send_message(message.chat.id, "Через час")
                    time.sleep(2)

                    keyboard = telebot.types.ReplyKeyboardMarkup()
                    key_bye = telebot.types.KeyboardButton(text="Пока")
                    keyboard.add(key_bye)

                    bot.send_message(message.chat.id, "Иван: Не повезло мне сегодня. Ну ладно, пока",
                                     reply_markup=keyboard)

                    bot.register_next_step_handler(message, alex)

                    def f_2_2(message):
                        bot.register_next_step_handler(message, alex)

                    bot.register_next_step_handler(message, f_2_2)

            elif call.data == '/Скажу':
                bot.send_message(call.message.chat.id, f'Дмитрий Евгеньевич: О, {player.player_name}, вы сделали')
                time.sleep(2)
                photo = open('../img/cubic_equation.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo=photo)
                time.sleep(1)
                bot.send_message(call.message.chat.id, f'Дмитрий Евгеньевич: Тогда решите это уравнение')

                def f_2_3(message):
                    try:
                        ans = sorted(list(map(int, message.text.split())))
                    except:
                        ans = -1
                    if ans == [57, 58, 239]:
                        bot.send_message(message.chat.id, "Дмитрий Евгеньевич: Замечательно. Все правильно")
                        time.sleep(1)
                        bot.send_message(message.chat.id, player.intelligence(5))
                        player.rep(10)
                    else:
                        bot.send_message(message.chat.id, 'Дмитрий Евгеньевич: Неправильно! Садитесь, 2!')
                        bot.send_message(message.chat.id, player.intelligence(-5))
                        player.rep(-10)
                    time.sleep(2)
                    bot.send_message(message.chat.id, 'Через час')
                    alex(message)

                bot.register_next_step_handler(message, f_2_3)



    elif message.text == "Возможно частично":
        bot.send_message(message.chat.id, "Иван: Ха-ха, понял",
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        time.sleep(1)
        bot.send_message(message.chat.id, "10 минут спустя")
        time.sleep(1)

        keyboard = telebot.types.ReplyKeyboardMarkup()
        key_probably = telebot.types.KeyboardButton(text="Я только часть дз сделал")
        key_yes = telebot.types.KeyboardButton(text="Да")
        keyboard.add(key_probably, key_yes)

        bot.send_message(message.chat.id,
                         f"Дмитрий Евгеньевич: {player.player_name}, вы сделали домашку?", reply_markup=keyboard)

        def f_2_4(message):
            if message.text == "Я только часть дз сделал":
                bot.send_message(message.chat.id,
                                 f"Дмитрий Евгеньевич: Тогда покажите Александре Игоревне то, что сделали")
                time.sleep(2)
                bot.send_message(message.chat.id, "15 минут спустя")
                time.sleep(1)
                bot.send_message(message.chat.id,
                                 f"Александра Игоревна: В том, что вы сделали, ошибок нет")
                time.sleep(1)
                bot.send_message(message.chat.id, "Час спустя")
                time.sleep(1)
                alex(message)
            if message.text == "Да":
                bot.send_message(message.chat.id,
                                 f"Дмитрий Евгеньевич: Тогда покажите Александре Игоревне тетрадь")

                keyboard = telebot.types.ReplyKeyboardMarkup()
                key_forgot = telebot.types.KeyboardButton(text="Я дома забыл")
                key_no = telebot.types.KeyboardButton(text="Я не успел его сделать")
                keyboard.add(key_forgot, key_no)

                time.sleep(2)
                bot.send_message(message.chat.id, "Александра Игоревна: Так, а где номер 09.10?",
                                 reply_markup=keyboard)

                def f_3_1_1(message):
                    if message.text == "Я дома забыл":
                        if player.params[2] > 0:
                            bot.send_message(message.chat.id, ("У вас хорошо прокачено красноречие! "
                                                               "Вы убедили Александру Игоревну, что забыли задание дома "))
                            bot.send_message(message.chat.id, "Александра Игоревна: Ладно, в пятницу принесете ")
                            bot.send_message(message.chat.id, player.eloquence(5))
                        else:
                            bot.send_message(message.chat.id, "Александра Игоревна: Не надо врать!")
                            bot.send_message(message.chat.id, player.health(-5))
                    else:
                        bot.send_message(message.chat.id, "Александра Игоревна: Ладно, в пятницу принесете")

                    time.sleep(1)
                    bot.send_message(message.chat.id, 'Через час')
                    alex(message)

                bot.register_next_step_handler(message, f_3_1_1)

        bot.register_next_step_handler(message, f_2_4)

    elif message.text == "Нет, я не успел":
        time.sleep(1)
        bot.send_message(message.chat.id, "Александра Игоревна: Я вообще-то все слышу")
        time.sleep(1)
        bot.send_message(message.chat.id,
                         "Александра Игоревна: Не успевают только неуспевающие.. Принесете к следующему уроку")
        time.sleep(1)
        bot.send_message(message.chat.id, player.health(-5))
        time.sleep(1)
        bot.send_message(message.chat.id, player.eloquence(-5))

        time.sleep(1)
        bot.send_message(message.chat.id, 'Через час')
        time.sleep(1)
        alex(message)




def f_3(message):
    time.sleep(1)
    if message.text == "Да, пойду":
        bot.send_message(message.chat.id, "Алексей: Отлично, тогда пошли", reply_markup=telebot.types.ReplyKeyboardRemove())
        time.sleep(2)
        bot.send_message(message.chat.id, "Это решение положительно сказалось на вашем красноречии!")
        time.sleep(1)
        bot.send_message(message.chat.id, player.eloquence(15))
        time.sleep(2)
        bot.send_message(message.chat.id, "Но оно уменьшило продолжительность отдыха")
        time.sleep(1)
        bot.send_message(message.chat.id, player.health(-5))
        time.sleep(1)

    else:
        bot.send_message(message.chat.id, "Алексей: Ну тогда до завтра", reply_markup=telebot.types.ReplyKeyboardRemove())
        time.sleep(2)
        bot.send_message(message.chat.id, "Это хорошо повлияет на ваш сон!")
        time.sleep(1)
        bot.send_message(message.chat.id, player.health(10))
        time.sleep(2)
        bot.send_message(message.chat.id, "Но ваш навык красноречия будет уменьшен!")
        time.sleep(1)
        bot.send_message(message.chat.id, player.eloquence(-5))
    time.sleep(1)
    f_4(message)

def f_4(message):
    bot.send_message(message.chat.id, "Продолжение следует...")


if __name__ == '__main__':
    bot.polling(True)
