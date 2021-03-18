from gtts import gTTS
import PyPDF2

## Quick Settings
# Name of the book without extension, must be on PWD
#bookname =  input('Book name (Without extension): ')
bookname =  'redes de computadora'

# Language of the book
# Run gTTS-cli --all to check for available languages
#language =  input('Book languaje (es, en): ')
language =  'es'

# Page where the file is going to start reading
# Leave 0 to read all 
#startPage = int(input('Starting page: ') )
startPage = 26

## PDF proccesing
#Create a pdf file object
# Add extension .pdf to a the filename
pdf = open(bookname + '.pdf', 'rb')

#Create a pdf reader object
pdf_reader = PyPDF2.PdfFileReader(pdf)

# Count the total number of pages in the document
pages = pdf_reader.numPages
endPage = 27
#endPage = int(input('Ending page(blank for all, max {}): '.format(pages)))

if endPage == "":
    endPage = pages


# Variable where text is going to be stored
textList = []

# Extracting data from each page
for pageNumber in range(startPage , endPage):
    try:
        page = pdf_reader.getPage(pageNumber)

        #Convert multiple lines to a single string
        textString = page.extractText()

        #Remove Newline characters
        textString = textString.replace('\n', '')

        #Remove Newline characters
        textString = textString.replace('-', '')

        #Convert text to audio
        audio = gTTS(text=textString, lang=language, slow=False)

        #Save audio as mp3 file
        audio.save(bookname+"-page-{}".format(pageNumber)+'.mp3')
        print(bookname+"-page-{}".format(pageNumber)+'.mp3 Created')

    except:
        print(bookname+"-page-{}".format(pageNumber)+'.mp3 Not Created')

