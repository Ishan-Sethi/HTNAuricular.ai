import requests
import json
import AudioUpload
from wit import Wit

def pretty_print(response_json: json):
    print(json.dumps(response_json, indent=4, sort_keys=True))

def sendResponses(responses):
    client = Wit('C56EAX6MPKJ5NDESA5RZ5JIUPGC5NDZP')
    data = []
    for sentence in responses:
        for phrase in sentence:
            response = client.message(phrase)
            pretty_print(response)
            data.append(str(response))
    return data

responses = AudioUpload.sendAudio("./test audio/aryan is teacher 1.wav")
print (responses)
print(sendResponses(responses))
