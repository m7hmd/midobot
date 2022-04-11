import requests, user_agent, json, flask, telebot, random, os, sys, time
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "5133056238:AAGluF9S2vYrxmVkSjykww0KUOf7B6dSB3c"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
w = ['1', "2","3","4",'5', "6","7","8",'9', "0","q","w",'e', "r","t","y",'u', "i","o","p",'a', "s","d","f","g","h",'j', "k","l","z",'x', "c","v","b",'n', "m"]
@bot.message_handler(content_types=["text"])
def gen(message):
    if "/" not in message.text:
        z = message.text[0]
        n = len(message.text)
        n2 = n - 1
        lists = []
        for n in range(n):
            list = []
            for i in range(n2):
                (list.append(z))
            list.insert(n, '*')
            lists.append("".join(list))
        for word in lists:
            m = ''
            a = []
            for i in w:
                a.append(word.replace("*", i) + "\n")
            bot.send_message(message.chat.id, m.join(a))
    else:
        bot.send_message(message.chat.id, "Send Test Like : zzzz")
   
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://listmakerfz.herokuapp.com/" + str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
