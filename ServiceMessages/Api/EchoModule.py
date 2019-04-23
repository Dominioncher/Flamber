from autobahn.wamp import CallOptions

from Core.Core import api


@api.register('echo')
def echo(message):
    return message
