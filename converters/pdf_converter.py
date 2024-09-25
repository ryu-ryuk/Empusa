from PyPDF2 import PdfReader, PdfWriter
import os
import argparse

def compress_pdf(input_pdf_path, output_pdf_path):
    """
    Compress a PDF file by copying its pages.
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        writer.add_page(page)

    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Compressed {input_pdf_path} to {output_pdf_path}")

# Main function for command-line use
def main():
    """
    Command-line argument parsing and execution for PDF compression.
    """
    parser = argparse.ArgumentParser(description="Compress a PDF file.")
    parser.add_argument('--input', type=str, required=True, help="Path to the input PDF file.")
    parser.add_argument('--output', type=str, required=True, help="Path to save the compressed output PDF file.")

    args = parser.parse_args()

    input_pdf_path = args.input
    output_pdf_path = args.output

    if not os.path.exists(input_pdf_path):
        print(f"Error: {input_pdf_path} does not exist.")
        return

    compress_pdf(input_pdf_path, output_pdf_path)

if __name__ == "__main__":
    main()
