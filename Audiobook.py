import pyttsx3
import PyPDF2
book = open('Rewire Your Brain.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
friend = pyttsx3.init()
for num in range(24,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    friend.say(text)
    friend.runAndWait()