from pdf2docx import Converter

pdf_File = r'C:\Users\User\Desktop\PDF Converter\test.pdf'
doc_file = r'C:\Users\User\Desktop\PDF Converter\test.doc'

cv = Converter(pdf_File)
cv.convert(doc_file)
cv.close()
