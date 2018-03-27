# -*- coding: utf-8 -*-
import coms
import telebot
from telebot import types

bot = telebot.TeleBot(coms.token)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Наши проекты🎭']])
    bot.send_message(m.chat.id,"""⚡ В связи возможной блокировкой Telegram на территории РФ мы нашли решение. 
Прошу максимально распространить среди друзей и знакомых, дабы мы все не потеряли доступ к лучшему мессендеру на рынке. 
Коллеги, сделайте призывы в своих каналах тоже или просто репост этого сообщения. 
Есть бот @socks5_bot, который в несколько кликов позволяет установить внутренний VPN. 
Ниже прикладываю инструкцию как им воспользоваться. 
Канал автора с обновлениями по боту: @socks5ru 

1. Отправь боту /start, ты получишь приветственное сообщение. 
2. Нажми «Получить», чтобы получить список с серверами 
3. Выбери любой сервер, бот пришлет тебе данные для подключения 
4. После получения сообщения с данными для подключения, нажми кнопку «Подключить», чтобы подключиться к серверу.""", reply_markup=keyboard)


@bot.message_handler(regexp='Наши проекты🎭')
def project(m):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*[types.InlineKeyboardButton(text="🌸Miss Kazan🌸", url='http://t.me/misskazan')
    keyboard.add(*[types.InlineKeyboardButton(text='📺Новости Казань📺', url='http://t.me/newkzn')
    keyboard.add(*[types.InlineKeyboardButton(text="🎩Бизнес Казань🎩", url='http://t.me/bsnkzn')
    bot.send_message(m.chat.id, "Подписывайся на наши проекты✔️", reply_markup=keyboard)








bot.polling(none_stop=True, interval=1)




