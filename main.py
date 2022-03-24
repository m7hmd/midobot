import requests, user_agent, json, flask, telebot, random, os, sys, time
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

BOT_TOKEN = "1206956607:AAGApSGAcjNK_eKu8gad72IZgaNtKLV2fiQ"
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(content_types=["text"])
def S(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Send List ......")
    elif "/" in message.text:
        bot.send_message(message.chat.id, "Send List ......")
    else:
        mes = message.text.splitlines()
        for username in mes:
            username1 = username.replace("@", "")
            url = "https://tamtam.chat/" + str(username1)
            headers = {
                "User-Agent": generate_user_agent(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}
            response = requests.get(url, headers=headers)
            if "Public channel" in response.text or "Open channel" in response.text:
                if 'data-url="' in response.text:
                    responseTime = requests.get(str((response.text.split('data-url="')[1]).split('">')[0])).text.split("<time>")[1].split(" </time>")[0]
                    bot.send_message(message.chat.id, f"URL :: {url}\nTime :: {responseTime.replace('января в','1').replace('февраля','2').replace('марта','3').replace('мая','5').replace('июля','7').replace('августа','8').replace('октября','10') .replace('июня','6')}")
                else:
                    bot.send_message(message.chat.id, f"URL :: {url}\nTime :: Don't Have Post")
            time.sleep(5)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://bottttelegram.herokuapp.com/" + str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
