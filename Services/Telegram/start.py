import asyncio
from Core.Scripts import connect
from Services.Telegram.Scripts.TelegramBot import dp


loop = asyncio.get_event_loop()
loop.create_task(dp.start_polling(reset_webhook=True))
connect("ws://crossbar-wamp-router.herokuapp.com/ws")
