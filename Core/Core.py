from functools import wraps

from autobahn.asyncio.component import Component
from autobahn.wamp import PublishOptions, RegisterOptions


class Api(Component):
    def publish(self, topic, *args, clients=None):
        self._session.publish(topic, *args, options=PublishOptions(eligible=clients))

    def call(self, procedure, *args, **kwargs):
        self._session.call(procedure, *args, **kwargs)

    def register(self, uri, options=None):
        assert options is None or isinstance(options, RegisterOptions)

        if options is None:
            options = RegisterOptions(details=True)

        def decorator(fn):
            def do_registration(session, details):
                return session.register(fn, procedure=uri, options=options)

            self.on('join', do_registration)
            return fn

        return decorator


api = Api()
