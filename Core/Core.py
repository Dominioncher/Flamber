import inspect

from autobahn.asyncio.component import Component
from autobahn.wamp import PublishOptions, RegisterOptions


class Api(Component):
    # def publish(self, topic, *args, clients=None):
    #     self._session.publish(topic, *args, options=PublishOptions(eligible=clients))
    #
    # def call(self, procedure, *args, **kwargs):
    #     self._session.call(procedure, *args, **kwargs)

    def register(self, uri, options=None):
        assert options is None or isinstance(options, RegisterOptions)

        def decorator(fn):
            new_options = options
            fn_args = inspect.getfullargspec(fn).args
            if 'details' in fn_args:
                if options is None:
                    new_options = RegisterOptions(details=True)
                else:
                    new_options.details = True

            def do_registration(session, details):
                return session.register(fn, procedure=uri, options=new_options)

            self.on('join', do_registration)
            return fn
        return decorator


api = Api()
