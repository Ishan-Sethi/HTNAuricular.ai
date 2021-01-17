import requests
import json
import AudioUpload
from wit import Wit


def sendResponses(responses):
    client = Wit('C56EAX6MPKJ5NDESA5RZ5JIUPGC5NDZP')
    data = []
    for result in responses:
        response = client.message(result)
        print(str(response))
        data.append(str(response))
    return data

responses = AudioUpload.sendAudio("Recording_2.wav")
print (responses)
print(sendResponses(responses))
