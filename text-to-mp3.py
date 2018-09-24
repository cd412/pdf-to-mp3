from gtts import gTTS
import os

language = 'en'
slow = False
inputFile = 'text-data.txt'
outputFile = 'audio-data.mp3'


def getTts():
    with open(inputFile, 'r') as myfile:
        term = myfile.read()
    return gTTS(text=term, lang=language, slow=slow)


def writeMp3(tts, outputFile):
    with open(outputFile, 'wb') as fp:
        tts.write_to_fp(fp)

def openFile():
    os.system(outputFile)


writeMp3(getTts(), outputFile)
openFile()




