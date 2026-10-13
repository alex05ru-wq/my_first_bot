# Telegram-бот «Эхо»

Мой первый Telegram-бот на Python. Отвечает на команду /start и повторяет любое текстовое сообщение пользователя.

## Возможности

- Команда /start — приветствие с именем пользователя
- Эхо-ответ на любое текстовое сообщение
- Токен бота хранится в .env (не попадает в репозиторий)

## Технологии

- Python 3
- pyTelegramBotAPI — библиотека для работы с Telegram Bot API
- python-dotenv — загрузка токена из .env

## Установка и запуск

1. Клонируй репозиторий:

git clone https://github.com/alex05ru-wq/my_first_bot.git
cd my_first_bot

2. Установи зависимости:

pip install pyTelegramBotAPI python-dotenv

3. Создай файл .env в корне проекта и добавь свой токен от @BotFather:

BOT_TOKEN=твой_токен

4. Запусти бота:

python bot.py

5. Открой своего бота в Telegram и напиши /start.

## Структура проекта

my_first_bot/
├── bot.py
├── .env
├── .gitignore
└── README.md

## Автор

Alex — https://github.com/alex05ru-wq
  



