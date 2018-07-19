from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

input1 = open("files/document1.pdf", "rb")
input2 = open("files/document2.pdf", "rb")
input3 = open("files/document3.pdf", "rb")

merger.append(input1)
merger.append(input2)
merger.append(input3)

# Write to an output PDF document
output = open("files/document-output.pdf", "wb")
merger.write(output)