from google.cloud import speech
from google.cloud import storage
from google.oauth2 import service_account
from pydub import AudioSegment
import io
import os
import wave
credentials = service_account.Credentials.from_service_account_file("C:/Users/Ishan/Downloads/auricular-ai-2edefb9bcdf3.json") # change to credentials
def stereoToMono(fileName):
    audio = AudioSegment.from_wav(fileName)
    audio = audio.set_channels(1)
    audio.export(fileName, format="wav")

def getFramerateChannel(fileName):
    with wave.open(fileName, "rb") as file:
        print(file.getnchannels(), file.getframerate())
        return file.getframerate(), file.getnchannels()

def bucketUpload(fileName):
    storageClient = storage.Client(credentials=credentials, project="auricular-ai")
    bucket = storageClient.get_bucket("auricular-ai-audio-files")
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

def bucketDelete(fileName):
    storageClient = storage.Client(credentials=credentials, project="auricular-ai")
    bucket = storageClient.get_bucket("auricular-ai-audio-files")
    blob = bucket.blob(fileName)
    blob.delete()

def sendAudio(fileName):
    frameRate, channels = getFramerateChannel(fileName)
    if channels > 1:
        stereoToMono(fileName)
    bucketUpload(fileName)
    gcs_uri = 'gs://auricular-ai-audio-files/' + fileName
    transcript = ''
    client = speech.SpeechClient(credentials=credentials)
    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(sample_rate_hertz=frameRate, language_code='en-US')
    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=10000)
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))