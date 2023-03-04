"""
Главный модуль бота.
Функции старта и отправки выбранных фотографий.
Допфункции получения и удаления фото

Создатель Александр Говорухин, @alexitsochi
"""
import logging
import os
from aiogram import Bot, Dispatcher, executor, types

import db_methods
import image


logging.basicConfig(level=logging.INFO)
# Читаем ключ
with open('token.txt', 'r') as token:
    token_key = token.read()
# Создаем бота
bot = Bot(token=token_key)
dp = Dispatcher(bot)

kpp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_photo(kpp_id):
    # Получение фото из базы в папку cache. Отрисовка времени и геопозиции.
    db_methods.read_blob_data(kpp_id)
    global count_files
    count_files = os.listdir(path="cache")
    for images in count_files:
        image.create_img(images)


def rm_photo():
    # Очистка папки cache
    for f in os.listdir(path="cache"):
        os.remove(os.path.join("cache", f))


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.reply(f"Привет {user}, напиши номер кпп в числовом формате")


@dp.message_handler()
async def echo(message: types.Message):
    if message.text in str(kpp_list):
        await message.answer(f"Выбрано кпп-{message.text}")
        get_photo(message.text)
        for i in count_files:
            await message.answer_photo(open(f"cache/{i}", "rb"), caption=f"kpp{int(message.text)}")
        rm_photo()
    else:
        await message.answer("Такого кпп нет")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
