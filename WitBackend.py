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
    intent_only = []
    for sentence in data:
        if sentence['intents']:
            text = sentence['text']
            aricule = []
            dates = []
            if 'htn_auricule:htn_auricule' in sentence['entities']:
                for entities in sentence['entities']['htn_auricule:htn_auricule']:
                    ariculi = dict(body=entities['body'], confidence=entities['confidence'])
                    aricule.append(ariculi)
            if 'wit$datetime:datetime' in sentence['entities']:
                for entities in sentence['entities']['wit$datetime:datetime']:
                    date = dict(body=entities['body'], confidence=entities['confidence'], value=entities['value'])
                    dates.append(date)
            final_data = [text, aricule, dates]
            intent_only.append(json.dumps(final_data))
    return intent_only
