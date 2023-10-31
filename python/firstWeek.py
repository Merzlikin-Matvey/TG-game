import telebot

def day1(bot: telebot.Telebot, message):
    bot.send_message(message.chat.id, '9:00. 229 кабинет, алгебра')
    