import requests
import json
import AudioUpload
def sendResponses(responses):
    endpoint = "https://api.wit.ai/message"
    accessToken = "C56EAX6MPKJ5NDESA5RZ5JIUPGC5NDZP"
    data = []
    headers = {'authorization': 'Bearer ' + accessToken}
    for result in responses.results:
        if result.alternatives[0].confidence > 90:
            response = requests.get(endpoint % result.alternatives[0].transcript, headers=headers)
            data.append(json.load(response.content))
    return data

responses = AudioUpload.sendAudio("Recording_2.wav")

print(sendResponses(responses))
