#Libraries

import PyPDF2
import os
from gtts import gTTS #google's library
import pyttsx3

fileType = 'pdf'
lang = 'en'

initalizer_py = pyttsx3.init()

pdfFile = open('sample.{type}'.format(type=fileType), 'rb')
pdfRead = PyPDF2.PdfFileReader(pdfFile)

print(pdfRead.numPages)
# pageObj = pdfRead.getPage(10)
# print(pageObj.extractText())

initalizer_py.setProperty('rate', 150)
initalizer_py.setProperty('volume', 0.8)
# initalizer_py.setProperty('voice', voice.id)

voices = initalizer_py.getProperty('voices')

for voice in voices:
    initalizer_py.setProperty('voice', voice.id)
    initalizer_py.say('sample pdf.')


# textObj = gTTS(text=pageObj.extractText(), lang=lang, slow=False)
# textObj.save('book.mp3')
# os.system("save book.mp3")
initalizer_py.runAndWait()
pdfFile.close()
