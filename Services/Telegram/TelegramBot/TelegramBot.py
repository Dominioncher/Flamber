from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import DialogFlow.DialogFlow as df
import io

import YandexSpeehKit.YandexSpeechKit as sk

TOKEN = '629170974:AAFLLbCM0WduQy-2oHwKFYeY5-RHiJCr4qI'

PROXY_1 = 'socks4://103.77.159.214:4145'
PROXY_2 = 'http://84.242.188.162:38182'
PROXY_3 = 'socks4://23.252.66.1:54321'
PROXY_4 = 'http://94.75.76.10:8080'
PROXY_5 = ''
PROXY_6 = ''
PROXY_7 = ''
PROXY_8 = ''
PROXY_9 = ''
REQUEST_KWARGS = {
    'proxy_url': PROXY_3
}


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')


def textMessage(bot, update):
    text = update.message.text
    try:
        answer = df.textMessage(text)
    except:
        answer = 'Я вас не поняла, Вы можете повторить свой запрос?'
    bot.send_message(chat_id=update.message.chat_id, text=answer)


def audioMessage(bot, update):
    file = update.message.voice.file_id
    audio = bot.get_file(file)
    bytesVoice = audio.download_as_bytearray()
    try:
        text = sk.speech_to_text(bytes=bytesVoice)
        answer = df.textMessage(text)
    except:
        answer = 'Я вас не поняла. Вы можете повторить свой запрос?'

    audioAnswer = sk.text_to_speech(answer)
    bot.send_voice(chat_id=update.message.chat_id, voice=audioAnswer)


updater = Updater(token=TOKEN, request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher


# Хендлеры
# start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)
audio_message_handler = MessageHandler(Filters.voice, audioMessage)
# Добавляем хендлеры в диспетчер
# dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)
dispatcher.add_handler(audio_message_handler)
# Начинаем поиск обновлений
updater.start_polling(clean=True)
# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
