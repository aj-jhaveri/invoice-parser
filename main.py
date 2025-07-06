import os
import logging
import argparse
from extractors.pdf_extractor import extract_text_from_pdf
from extractors.ocr_extractor import extract_text_from_image_pdf
from parsers.invoice_parser import parse_invoice_data
from outputs.csv_writer import write_to_csv

logging.basicConfig(level=logging.INFO)

def process_invoices(invoice_dir, output_csv):
    """Processes all PDF invoices in a directory."""
    all_data = []
    for filename in os.listdir(invoice_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(invoice_dir, filename)
            logging.info(f"Processing {pdf_path}...")

            # Try text extraction first
            text = extract_text_from_pdf(pdf_path)

            # If text extraction fails, try OCR
            if not text or len(text.strip()) < 50: # Basic check for empty/failed extraction
                logging.warning(f"Text extraction for {pdf_path} was insufficient, trying OCR.")
                text = extract_text_from_image_pdf(pdf_path)

            if text:
                data = parse_invoice_data(text)
                data['filename'] = filename
                all_data.append(data)
            else:
                logging.error(f"Could not extract text from {pdf_path}")

    write_to_csv(all_data, output_csv)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Invoice Parser")
    parser.add_argument("-i", "--input_dir", default="sample_invoices", help="Input directory with invoices")
    parser.add_argument("-o", "--output_file", default="invoices.csv", help="Output CSV file")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    invoice_dir = os.path.join(script_dir, args.input_dir)
    output_csv = os.path.join(script_dir, args.output_file)

    process_invoices(invoice_dir, output_csv)
