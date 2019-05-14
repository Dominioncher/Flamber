import io
import xml.etree.ElementTree as XmlElementTree
import uuid

import httplib2
import requests

YANDEX_API_KEY = '069b6659-984b-4c5f-880e-aaedcfd84102'
YANDEX_ASR_HOST = 'asr.yandex.net'
YANDEX_ASR_PATH = '/asr_xml'
TTS_URL = "https://tts.voicetech.yandex.net/generate"
CHUNK_SIZE = 1024 ** 2


def read_chunks(chunk_size, bytes):
    while True:
        chunk = bytes[:chunk_size]
        bytes = bytes[chunk_size:]

        yield chunk

        if not bytes:
            break


def speech_to_text(bytes, request_id=uuid.uuid4().hex, topic='notes', lang='ru-RU', key=YANDEX_API_KEY):
    # Формирование тела запроса к Yandex API
    url = YANDEX_ASR_PATH + '?uuid=%s&key=%s&topic=%s&lang=%s' % (
        request_id,
        key,
        topic,
        lang
    )

    # Считывание блока байтов
    chunks = read_chunks(CHUNK_SIZE, bytes)

    # Установление соединения и формирование запроса
    connection = httplib2.HTTPConnectionWithTimeout(YANDEX_ASR_HOST)
    connection.connect()
    connection.putrequest('POST', url)
    connection.putheader('Transfer-Encoding', 'chunked')
    connection.putheader('Content-Type', 'audio/ogg;codecs=opus')
    connection.endheaders()

    # Отправка байтов блоками
    for chunk in chunks:
        connection.send(('%s\r\n' % hex(len(chunk))[2:]).encode())
        connection.send(chunk)
        connection.send('\r\n'.encode())
    connection.send('0\r\n\r\n'.encode())
    response = connection.getresponse()

    # Обработка ответа сервера
    if response.code == 200:
        response_text = response.read()
        xml = XmlElementTree.fromstring(response_text)

        if int(xml.attrib['success']) == 1:
            max_confidence = - float("inf")
            text = ''

            for child in xml:
                if float(child.attrib['confidence']) > max_confidence:
                    text = child.text
                    max_confidence = float(child.attrib['confidence'])

            if max_confidence != - float("inf"):
                return text
    raise Exception


def text_to_speech(text, speaker="tanya", audio_format='mp3', key=YANDEX_API_KEY, lang='ru-RU'):
    params = {
        "speaker": speaker,
        "format": audio_format,
        "key": key,
        "lang": lang,
        "text": text
    }

    data = requests.get(TTS_URL, params=params, stream=False)

    return data.content

