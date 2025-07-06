import pdfplumber
import logging

logging.basicConfig(level=logging.INFO)

def extract_text_from_pdf(pdf_path):
    """Extracts text from a text-based PDF."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            return "\n".join(page.extract_text() for page in pdf.pages)
    except Exception as e:
        logging.error(f"Error extracting text from {pdf_path}: {e}")
        return None
