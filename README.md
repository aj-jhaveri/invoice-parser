# Invoice Parser

A robust command-line tool to automatically extract key information from PDF invoices. This tool can intelligently handle both digitally created and scanned (image-based) invoices, saving the extracted data to a CSV file.

This project is designed to automate the tedious task of manual data entry from invoices, making it a practical tool for business-related workflows.

## Key Features

- **Dual Extraction Strategy:** Automatically detects the best method for data extraction. It first attempts to read text directly from the PDF and, if that fails, seamlessly switches to Optical Character Recognition (OCR).
- **Flexible & Configurable:** Use command-line arguments to specify your input and output locations.
- **Core Data Extraction:** Parses the text to find four key fields: Invoice Number, Vendor Name, Invoice Date, and Total Amount.
- **Well-Tested:** Includes a suite of unit tests to ensure the core parsing logic is reliable and accurate.
- **Clean & Extensible Structure:** The project is organized logically into modules for extraction, parsing, and output, making it easy to maintain and extend.

## How It Works

The script iterates through all PDF files in a specified directory. For each file, it employs a two-step extraction process:

1.  **Text-Based Extraction:** It first uses the `pdfplumber` library to try and extract text directly. This works best for digitally-created PDFs.
2.  **OCR Fallback:** If the initial extraction yields insufficient text (a common sign of a scanned document), the script automatically uses `pdf2image` to convert the PDF pages into images and then runs Google's Tesseract OCR engine (`pytesseract`) to "read" the text from the images.

Once the text is extracted, a series of regular expressions are used to parse and find the required data fields.

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

First, clone this repository to your local machine.

```bash

git clone https://github.com/aj-jhaveri/invoice-parser.git
cd invoice-parser
```

### 2. System-Level Dependencies

This tool relies on two external programs: **Tesseract OCR** and **Poppler**.

**For Debian/Ubuntu:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr poppler-utils
```

**For macOS (using Homebrew):**
```bash
brew install tesseract poppler
```

**For Windows:**
Installation instructions can be found here:
- **Tesseract:** [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
- **Poppler:** [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)

### 3. Python Environment and Dependencies

It is highly recommended to use a Python virtual environment to manage project dependencies.

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# On Windows, use:
# venv\Scripts\activate

# Install the required Python packages
pip install -r requirements.txt
```

## Usage

To run the parser, use the `main.py` script from your terminal.

### Command-Line Arguments
- `-i` or `--input_dir`: The directory containing your PDF invoices. Defaults to `sample_invoices`.
- `-o` or `--output_file`: The path for the output CSV file. Defaults to `invoices.csv`.

### Example

1.  Place your PDF invoices into the `sample_invoices` directory (or any other directory).
2.  Run the script:

    ```bash
    # Use the default input and output locations
    python main.py

    # Specify a different input directory and output file
    python main.py -i /path/to/your/invoices -o extracted_data.csv
    ```
3.  The extracted data will be saved in the CSV file you specified.

## Running Tests

This project includes a set of unit tests to verify the parsing logic. To run the tests, execute the following command from the project's root directory:

```bash
python -m unittest tests/test_parser.py
```
If all tests pass, you will see an "OK" message. This is a great way to ensure the core functionality is working as expected, especially after making changes to the code.
