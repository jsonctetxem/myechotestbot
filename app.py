import os
import telebot
import random
from flask import Flask, request

bot = telebot.TeleBot(os.environ['token'])

server = Flask(__name__)

text = ['Да','Нет','Незнаю','Возможно','100%']

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, 'Привет, отправь мне вопрос и я скажу да или нет')


@bot.message_handler(content_types=['text'])
def send_text(message):
	bot.reply_to(message, random.choice(text))


@server.route('/', methods=['POST'])
def webhook():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "!", 200


if __name__ == '__main__':
	server.run()