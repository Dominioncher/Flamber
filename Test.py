import asyncio

from autobahn.asyncio import ApplicationSession


class Component(ApplicationSession):
    async def onJoin(self, details):
        # a remote procedure; see frontend.py for a Python front-end
        # that calls this. Any language with WAMP bindings can now call
        # this procedure if its connected to the same router and realm.
        def add2(x, y):
            return x + y
        reg = await self.register(add2, u'com.myapp.add2')
        print("registered 'com.myapp.add2' with id {}".format(reg.id))

        # publish an event every second. The event payloads can be
        # anything JSON- and msgpack- serializable
        while True:
            self.publish(u'com.myapp.hello', 'Hello, world!')
            await asyncio.sleep(1)
