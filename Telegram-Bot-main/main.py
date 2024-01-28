#библиотеки, которые загружаем из вне
import telebot
import random

# Токен вашего бота, полученный от BotFather
TOKEN = '6748227718:AAEPyRwol6nqiLJ5TOOUuyEQO0vStfzDOXo'

# Список книг
books = [
    'https://disk.yandex.ru/i/HmGtacktF_kI_A',
    'https://disk.yandex.ru/i/jijlghK2YlL0VQ',
    'https://disk.yandex.ru/i/J9cPmHR7PemC5w',
    'https://disk.yandex.ru/i/U_9cTytBOHIkSw',
    'https://disk.yandex.ru/i/uqFOCiYJj6AasQ',
    'https://disk.yandex.ru/i/67FszUxA1KOL2Q',
    'https://disk.yandex.ru/d/HKZDAA7kW2-rjQ',
    'https://disk.yandex.ru/d/kzBD3m-6y-w0xA',
    'https://disk.yandex.ru/i/1RsKWobC9jY-bA',
    'https://disk.yandex.ru/i/O6Vd6Xkh7K2iXg',
    'https://disk.yandex.ru/d/Elgmx3ZB7pPIcg', 
    'https://disk.yandex.ru/i/_kyeclF3UWNPuA', 
    'https://disk.yandex.ru/i/HjOMAhbfqojAjQ',
    'https://disk.yandex.ru/i/647CyNsktwZseA',
    'https://disk.yandex.ru/i/clCsE1QedmOYWg'
]

# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привееееет! Я Лукбот для выбора книг. Нажми /getbook, чтобы получить случайную книгу.")

@bot.message_handler(commands=['getbook'])
def handle_getbook(message):
    # Выбираем случайную книгу из списка
    random_book = random.choice(books)
    bot.reply_to(message, f"Рекомендую тебе почитать эту книгу: {random_book}")

# Запускаем бота
bot.polling()