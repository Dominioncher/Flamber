from autobahn.wamp import RegisterOptions, PublishOptions, CallDetails

from Core.Core import api


@api.register('broadcast', RegisterOptions(details=True))
def broadcast(args, details: CallDetails):
    api._session.publish('broadcast_message', args, options=PublishOptions(eligible=details.caller))
