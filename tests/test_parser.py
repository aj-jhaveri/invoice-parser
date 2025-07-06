
import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from parsers.invoice_parser import parse_invoice_data

class TestInvoiceParser(unittest.TestCase):

    def test_parse_invoice_data(self):
        text = """
        Invoice No: 12345
        Vendor: Test Vendor
        Date: 01/01/2025
        Amount Due: $1,234.56
        """
        expected_data = {
            "invoice_number": "12345",
            "vendor_name": "Test Vendor",
            "invoice_date": "01/01/2025",
            "total_amount": "1234.56"
        }
        self.assertEqual(parse_invoice_data(text), expected_data)

    def test_parse_invoice_data_with_different_format(self):
        text = """
        INVOICE
        From: Another Vendor Inc.
        Invoice Number: INV-67890
        Invoice Date: 2/28/2025
        Total: 500.00
        """
        expected_data = {
            "invoice_number": "INV-67890",
            "vendor_name": "Another Vendor Inc.",
            "invoice_date": "2/28/2025",
            "total_amount": "500.00"
        }
        self.assertEqual(parse_invoice_data(text), expected_data)

    def test_parse_invoice_data_with_messy_vendor_name(self):
        text = """
        Invoice No: 789-ABC
        Vendor: Messy Vendor Name with
        some other text on the same line
        Date: Mar 3, 2025
        Amount Due: $1.00
        """
        expected_data = {
            "invoice_number": "789-ABC",
            "vendor_name": "Messy Vendor Name with", # This is still not perfect, but better
            "invoice_date": "Mar 3, 2025",
            "total_amount": "1.00"
        }
        # This will fail initially, and we'll fix the parser to make it pass.
        self.assertEqual(parse_invoice_data(text), expected_data)


if __name__ == '__main__':
    unittest.main()
