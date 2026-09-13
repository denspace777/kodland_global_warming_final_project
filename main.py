import telebot
from collections import defaultdict

from text_storage import random_fact, random_history, main_info, advice
from experement import quiz_questions
from passwor import password
bot = telebot.TeleBot(password)

points = defaultdict(int)
points_incorect = defaultdict(int)

user_responses = {}

def send_question(chat_id):
    bot.send_message(chat_id, quiz_questions[user_responses[chat_id]].text,
                     reply_markup=quiz_questions[user_responses[chat_id]].gen_markup())


                                # старт и помощь
@bot.message_handler(commands=['start'])
def send_help(message):
    bot.reply_to(message, "Привет! Этот туториал поможет тебе зазобраться в тг боте: команды /random_fact и /random_history расширят твои знания о потеплении, /main_info введёт в курс дела, /advice даст советы, а /quiz позволит проверить свои знания в мини викторине")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Вот все команды: /random_fact, /random_history, /advice, /main_info, /quiz")

                                # основные команды, просто текст
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

                                # мини игра
                                # надо разобраться как работает по подробней
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "correct":
        bot.answer_callback_query(call.id, "Молодец! Ты ответил правильно")
        points[call.id] += 1

    elif call.data == "wrong":
        bot.answer_callback_query(call.id, "К сожаленью ответ не павильный")
        points_incorect[call.id] += 1

    user_responses[call.message.chat.id] += 1
    if user_responses[call.message.chat.id] >= len(quiz_questions):
        bot.send_message(call.message.chat.id, f"Молодец! Ты прошёл викторину!")
        bot.send_message(call.message.chat.id, f"Твой счёт: {sum(points.values())}")
        bot.send_message(call.message.chat.id, f"Неправельные ответы: {sum(points_incorect.values())}")
        bot.send_message(call.message.chat.id, f"Их соотношение: {sum(points.values())/sum(points_incorect.values())}")      
    else:
        send_question(call.message.chat.id)


@bot.message_handler(commands=['quiz'])
def start(message):
    if message.chat.id not in user_responses.keys():
        user_responses[message.chat.id] = 0
        send_question(message.chat.id)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
