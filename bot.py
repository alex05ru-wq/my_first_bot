import os
import telebot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Реагирует на команду /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Я эхо-бот. Напиши что-нибудь.')

# Реагирует на любой текст
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, f'Ты написал: {message.text}')

# Запуск бота
print('Бот запущен...')
bot.polling(none_stop=True)