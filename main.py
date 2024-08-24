import logging
from aiogram import Bot, Dispatcher
from config import dp
#from handlers import register_handlers
from database import create_table
from config import bot
import asyncio
import sys
print(sys.prefix)
# Запуск процесса поллинга новых апдейтов
async def main():

    # Запускаем создание таблицы базы данных
    await create_table()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())