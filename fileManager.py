import os
import json
from datetime import datetime

__all__ = ['writeFile', 'readFile', 'deleteFile']

def writeFile(jsonFile):
    now = datetime.now()
    timestamp = now.strftime("%Y.%m.%d-%H.%M.%S")
    write = open(os.path.expanduser("~")+"/auricular/"+timestamp+".acrai", 'w')
    jsonFile.update({'time': timestamp})
    json.dump(jsonFile, write)
    pass

def readFile(name):
    read = open(os.path.expanduser("~")+"/auricular/"+name+".acrai")
    return json.load(read)

def deleteFile(name):
    os.remove(os.path.expanduser("~")+"/auricular/"+name+".acrai")
    pass
