import json
from wit import Wit
import datetime

def pretty_print(response_json: json):
    print(json.dumps(response_json, indent=4, sort_keys=True))

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
    for jsonresponse in data:
        if 'wit$datetime:datetime' in jsonresponse['entities'] and 'htn_auricule:htn_auricule' in jsonresponse['entities'] and jsonresponse['entities']['wit$datetime:datetime'][0]['type'] != 'interval':
            print(jsonresponse['entities']['wit$datetime:datetime'][0]["value"])
            print(jsonresponse['entities']['htn_auricule:htn_auricule'][0]["value"])
            print(jsonresponse['entities']['htn_auricule:htn_auricule'][0]["confidence"])
            print(jsonresponse["text"])
            print("")