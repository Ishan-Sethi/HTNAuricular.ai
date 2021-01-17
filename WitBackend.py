import requests
import json
from wit import Wit

def pretty_print(response_json: json):
    print(json.dumps(response_json, indent=4, sort_keys=True))

def sendResponses(responses):
    client = Wit('S5LPGE54WVG6FQ4MWM5YZXVUCY6JDVGB')
    data = []
    for sentence in responses:
        for phrase in sentence:
            response = client.message(phrase)
            pretty_print(response)
            data.append(str(response))
    return data

def postJsonData(data):
    intent_only = []
    for sentence in data:
        if sentence['intents']:
            intent_only.append(sentence)
    return intent_only
