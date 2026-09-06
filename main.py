import telebot

from text_storage import random_fact, random_history, main_info, advice
from passwor import password
bot = telebot.TeleBot("KEY")

                                # старт и помощь
@bot.message_handler(commands=['start'])
def send_help(message):
    bot.reply_to(message, "Привет! Этот туториал поможет тебе зазобраться в тг боте: команды /random_fact и /random_history расширят твои знания о потеплении, /main_info введёт в курс дела, ")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Вот все команды: /random_fact, /random_history, /advice, /main_info,")


                                # основные команды
@bot.message_handler(commands=['random_fact'])
def send_help(message):
    bot.reply_to(message, random_fact())

@bot.message_handler(commands=['random_history'])
def send_help(message):
    bot.reply_to(message, random_history())

@bot.message_handler(commands=['main_info'])
def send_help(message):
    bot.reply_to(message, main_info())

@bot.message_handler(commands=['advice'])
def send_help(message):
    bot.reply_to(message, advice())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
