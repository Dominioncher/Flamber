import io
import json

from aiogram import Bot, Dispatcher, types
from Core import Core


PROXY_1 = 'socks5://91.105.233.236:1080'
bot = Bot(token="816605181:AAH69FgKAQVUq_i_uSuRAk5I6EkDeeTd7zE", proxy=PROXY_1)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await bot.send_message(message.chat.id, "Привет\n Я Алиса \n")


# @dp.message_handler()
# async def text_message(message: types.Message):
#     answer = await Core.api._session.call('api/v1/user_question', message.text)
#     await bot.send_message(message.chat.id, answer)


@dp.message_handler()
async def audio_message(message: types.Message):
    answer = await Core.api._session.call('api/v1/user_question', message.text)
    answer = await Core.api._session.call('api/v1/text_to_speech', answer)
    await bot.send_voice(message.chat.id, voice=io.BytesIO(answer))
