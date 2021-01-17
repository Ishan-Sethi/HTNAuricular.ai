import os
import json
from datetime import datetime

__all__ = ['getFileList', 'writeFile', 'readFile', 'deleteFile']

__path__ = os.path.expanduser("~")+"/auricular/"

def getFileList():
    return [file for file in os.listdir(__path__) if os.path.isfile(os.path.join(__path__, file))]

def writeFile(jsonFile):
    now = datetime.now()
    timestamp = now.strftime("%Y.%m.%d-%H.%M.%S")
    write = open(__path__+timestamp+".acrai", 'w')
    jsonFile.update({'time': timestamp})
    json.dump(jsonFile, write)
    pass

def readFile(name):
    return json.load( open(__path__+name) )

def deleteFile(name):
    os.remove(__path__+name)
    pass
