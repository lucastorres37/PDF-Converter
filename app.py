#transformar pdf to word
import PyPDF4
 
file_path = 'test.pdf'
with open(file_path, mode='rb') as f:

    reader = PyPDF4.PdfFileReader(f)

    output = []
    numPages = reader.getNumPages()
    cont = 0
    while (cont < numPages):
        
        page = reader.getPage(cont)

        print(page.getContents())
        
        output.append(page.extractText())
        
        cont += 1
        
    file = open('test.doc', mode='w')
    for i in output:
        file.write(i)
    file.close()