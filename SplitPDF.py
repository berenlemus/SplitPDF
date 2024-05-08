from PyPDF2 import PdfReader, PdfWriter
pdf_file_path = 'file 1.pdf'
pdf = PdfReader(pdf_file_path)

pages = [0, 2, 4]
pdfwriter = PdfWriter()

for page_num in pages:
    pdfwriter.add_page(pdf.pages[page_num])

with open('output.pdf', 'wb') as out:
    pdfwriter.write(out)

print('PDF file has been split.')
