

def answers(response_json):

    response = response_json['result']['fulfillment']['speech']
    intent_name = response_json['result']['metadata']['intentName']
    parameters = response_json['result']['parameters']

    if response:
        return response
    raise Exception
