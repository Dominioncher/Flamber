import asyncio
from aioconsole import ainput
from autobahn.wamp import CallOptions

from Core.Core import api


@api.subscribe('broadcast_message')
def new_message(message):
    print("New message: {0}".format(message))


@api.on_join
async def joined(session, details):
    while True:
        message = await ainput('Введите новое сообщение ')
        await session.call('broadcast', message)
        echo = await session.call('echo', message)
        print(echo)
        await asyncio.sleep(1)
