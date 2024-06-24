import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def extract_emails(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = email_pattern.findall(text)
    return emails

def main(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    emails = extract_emails(text)
    return emails

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Extract emails from a PDF file.")
    parser.add_argument("pdf_path", help="Path to the PDF file.")
    args = parser.parse_args()

    extracted_emails = main(args.pdf_path)
    print("Extracted emails:", extracted_emails)
