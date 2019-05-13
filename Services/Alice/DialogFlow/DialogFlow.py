import apiai
import json

from Services.Alice.DialogFlow.Answers import answers


def message(text):
    request = apiai.ApiAI('770e0a0a4d744f2cbd9afe6c620fbf76').text_request()  # Токен API к Dialogflow
    request.lang = 'ru'  # На каком языке будет послан запрос
    request.session_id = 'AliceAI'  # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = text  # Посылаем запрос к ИИ с сообщением от юзера

    response = json.loads(request.getresponse().read().decode('utf-8'))

    response = answers(response)

    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        return response

    raise Exception
