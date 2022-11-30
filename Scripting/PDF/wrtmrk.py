import PyPDF2

template = PyPDF2.PdfFileReader(open('Scripting\\PDF\\supper.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('Scripting\\PDF\\wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()
print(watermark)

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
        