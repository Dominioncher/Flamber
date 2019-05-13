import asyncio
from autobahn.wamp import CallOptions, ApplicationError

from Core.Core import api


@api.subscribe('broadcast_message')
def new_message(message):
    print("New message: {0}".format(message))


@api.on_join
async def joined(session, details):
      # while True:
        # message = await ainput('Введите новое сообщение ')
        # await session.call('broadcast', message)
        # echo = await session.call('echo', message)
        # print(echo)
        # await asyncio.sleep(1)
        try:
            await auth(session)
        except Exception as e:
            print("Error: {} {}".format(e, e.args))


async def auth(session):
    # register = await session.call('api/v1/register', 'Artyom', 'Artyom30000')
    # print(register)
    #  logout = await session.call('api/v1/logout')
    #  print(logout)

    # token = await session.call('api/v1/authentication', 'Artyom', 'Artyom30000')
    # print(token)
    # auth = await session.call('api/v1/authorization', token)
    # print(auth)
    # sessions = await session.call('api/v1/get_user_sessions', 1)
    # print(sessions)

    answer = await session.call('api/v1/user_question', 'Привет')
    print(answer)
    answer = await session.call('api/v1/user_question', 'Как дела?')
    print(answer)
    answer = await session.call('api/v1/user_question', 'Ты кто?')
    print(answer)
    answer = await session.call('api/v1/user_question', 'Пока')
    print(answer)
