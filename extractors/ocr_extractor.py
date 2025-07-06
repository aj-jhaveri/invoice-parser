import pytesseract
from pdf2image import convert_from_path
import cv2
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

def extract_text_from_image_pdf(pdf_path):
    """Extracts text from an image-based PDF using OCR."""
    try:
        images = convert_from_path(pdf_path)
        text = ""
        for i, image in enumerate(images):
            # Convert to grayscale and apply thresholding
            image_np = np.array(image)
            gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            
            # Denoise
            denoised = cv2.fastNlMeansDenoising(thresh, None, 10, 7, 21)

            text += pytesseract.image_to_string(denoised, config='--psm 6')
        return text
    except Exception as e:
        logging.error(f"Error extracting text from {pdf_path} with OCR: {e}")
        return None
