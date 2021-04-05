import PyPDF2
import os
from gtts import gTTS
import pyttsx3

#Put pdf in the -> (pdfs) 'folder'

class Application():
    def __init__(self):
        self.fileType = 'pdf'
        self.lang = ['en']
        self.fileName = str(input('Please enter the pdf name: '))
    def readFile(self, file):
        try:
            openFile = open('pdfs/' + self.fileName, 'rb')
            read = PyPDF2.PdfFileReader(openFile)
            print(read.numPages)
        except FileNotFoundError:
            print('File not found')
        except NotADirectoryError:
            print('Directory not found')

reader = Application()
reader.readFile('harry_potter.pdf')
