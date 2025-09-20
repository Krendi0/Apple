import telebot
from telebot.types import *
from dotenv import load_dotenv
import random

load_dotenv()
token = os.getenv("TOKEN")
bot = telebot.TeleBot(token)
dig = "⛏ Копать"
rarity = ["Старый", "Древний", "Доисторический"]
material = ["Железный", "Золотой", "Глиняный"]
item = ["Горшок", "Кубок", "Кувшин"]
promo = "Super_Promo2025"


@bot.message_handler(commands=['start'])
def start(msg: Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=False)
    kb.add(dig)
    bot.send_photo(chat_id=msg.chat.id,
                   photo="https://cdn-media.tass.ru/width/1200_4ce85301/tass/m2/uploads/i/20190625/5080143.jpg",
                   caption="Приветствую искатель, вам предоставляется возможность получить скидки и поучаствовать в раскопках древнего города.",
                   reply_markup=kb)
    bot.register_next_step_handler(msg, dig_func, kb)


def dig_func(msg: Message, kb: ReplyKeyboardMarkup):
    if msg.text == dig:
        if random.random() < 0.05:
            bot.send_message(chat_id=msg.chat.id, text=f"Вы получили промокод: {promo}", reply_markup=kb)
        else:
            bot.send_message(chat_id=msg.chat.id,
                             text=f"Поздравляю вы получили: {random.choice(rarity)} {random.choice(material)} {random.choice(item)}",
                             reply_markup=kb)
        bot.register_next_step_handler(msg, dig_func, kb)


bot.infinity_polling()
