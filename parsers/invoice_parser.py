import re

def parse_invoice_data(text):
    """Parses invoice data from text using regex."""
    data = {
        "invoice_number": None,
        "vendor_name": None,
        "invoice_date": None,
        "total_amount": None
    }

    # Regex patterns (these are examples and may need to be adjusted)
    invoice_number_pattern = re.compile(r'(?:Invoice No|Invoice Number)[:\s]*([\w-]+)')
    vendor_name_pattern = re.compile(r'(?:Vendor|From)[:\s]*([\w\s.]+?)(?:\n|Date:|Invoice Date:)')
    date_pattern = re.compile(r'(?:Date|Invoice Date)[:\s]*(\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s.]*\d{1,2}[,.]*\s*\d{4})')
    total_amount_pattern = re.compile(r'(?:Total|Amount Due)[:\s]*[$]?([\d,]+\.\d{2})')

    # Find matches
    invoice_number = invoice_number_pattern.search(text)
    if invoice_number:
        data["invoice_number"] = invoice_number.group(1)

    vendor_name = vendor_name_pattern.search(text)
    if vendor_name:
        data["vendor_name"] = vendor_name.group(1).strip()

    invoice_date = date_pattern.search(text)
    if invoice_date:
        data["invoice_date"] = invoice_date.group(1)

    total_amount = total_amount_pattern.search(text)
    if total_amount:
        data["total_amount"] = total_amount.group(1).replace(',', '')

    return data
