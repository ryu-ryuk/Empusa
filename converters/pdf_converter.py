from PyPDF2 import PdfReader, PdfWriter
import os

def compress_pdf(input_pdf_path, output_pdf_path):
    '''Compress a PDF file.'''
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)

    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Compressed {input_pdf_path} to {output_pdf_path}")
