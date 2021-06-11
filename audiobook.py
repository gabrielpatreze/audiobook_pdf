import pyttsx3
import PyPDF2

book = open('teste.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
#numero de paginas
num_pages = pdf_reader.numPages

play = pyttsx3.init()
print('Reproduzindo audiobook')

for num in range(0, num_pages):
    page = pdf_reader.getPage(num)

    data = page.extractText()

    play.say(data)

    play.runAndWait()





