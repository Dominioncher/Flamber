from autobahn.wamp import CallDetails
from Core.Core import api


@api.register('echo')
def echo(message):
    return message
