import json
from wit import Wit

def sendResponses(responses):
    print("Sending transcripts to wit.ai")
    client = Wit('S5LPGE54WVG6FQ4MWM5YZXVUCY6JDVGB')
    data = []
    for sentence in responses:
        for phrase in sentence:
            print(phrase)
            if len(phrase) <= 280:
                response = client.message(phrase)
                data.append(response)
    return data

def postJsonData(data):
    intent_only = []
    for sentence in data:
        if sentence['intents']:
            intent_only.append(sentence)
    final_data, entities = {}, {}
    for intent in intent_only:
        entities = {}
        for entity in intent['entities']:
            entities['body'] = entity['body']
            entities['confidence'] = entity['confidence']
            if entity['role'] == "datetime":
                entities['value'] = entity['value']
        final_data.append(entities)
    return final_data
