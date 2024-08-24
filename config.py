# Конфигурация бота
import logging
from aiogram import Bot, Dispatcher, types
import sys
print(sys.prefix)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Замените "YOUR_BOT_TOKEN" на токен, который вы получили от BotFather
API_TOKEN = '7486648409:AAHt3oZ7dKA5_yNljaezVxl_Bx4aa15C4oI'
# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()
# Зададим имя базы данных
DB_NAME = 'quiz_bot.db'