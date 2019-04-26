from autobahn.wamp import CallDetails

from Core.Core import api


@api.register('broadcast')
def broadcast(args, details: CallDetails):
    api.publish('broadcast_message', args, clients=details.caller)
