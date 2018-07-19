from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
from reportlab.pdfgen import canvas
from StringIO import StringIO
from reportlab.lib.pagesizes import A4

merger = PdfFileMerger()

# Using ReportLab to insert image into PDF
imgTemp = StringIO()
imgDoc = canvas.Canvas(imgTemp, pagesize=A4)

# Draw image on Canvas and save PDF in buffer
imgPath = "files/image1.jpg"
imgDoc.drawImage(imgPath, 0, 0) 
imgDoc.save()

# Use PyPDF to merge the image-PDF into the template
input1 = PdfFileReader(StringIO(imgTemp.getvalue()))

input2 = open("files/document2.pdf", "rb")

merger.append(input1)
merger.append(input2)

# Write to an output PDF document
output = open("files/document-output-image.pdf", "wb")
merger.write(output)