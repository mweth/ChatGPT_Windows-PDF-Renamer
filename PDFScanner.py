import os
import re
import requests
import pytesseract
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

API_ENDPOINT = 'https://api.openai.com/v1/chat/completions'  # replaced with correct GPT-3.5 turbo endpoint
API_KEY = 'sk-YOUR_API'  # replace with your OpenAI key

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}',
}

# Set the path for Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # adjust the path accordingly

def extract_first_page_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        first_page = reader.pages[0]
        text = first_page.extract_text()
    except Exception as e:
        logging.error(f"Failed to read PDF: {pdf_path}, error: {str(e)}")
        return ''

    if text.strip() == '':  # scanned PDF, use OCR
        try:
            images = convert_from_path(pdf_path, first_page=1, last_page=1)  # Only the first page
            text = pytesseract.image_to_string(images[0])
        except Exception as e:
            logging.error(f"Failed to convert PDF to image for OCR: {pdf_path}, error: {str(e)}")
            return ''

    return text[:1000]  # limit to first 1000 characters

def generate_filename(text):
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {"role": "system", "content": "You are a file naming tool.  You only respond with proposed file names compatible with windows 10.  If the file contains a date, you start the file name with YYYY-MM-DD_"},
            {"role": "user", "content": f"Based on the following text, propose a file name that accurately identifies the file: {text}"}
        ],
        'max_tokens': 60,
        'temperature': 0.3
    }
    response = requests.post(API_ENDPOINT, headers=headers, json=data)
    if response.status_code == 200:
        json_response = response.json()
        if 'choices' in json_response and len(json_response['choices']) > 0 and 'message' in json_response['choices'][0]:
            return json_response['choices'][0]['message']['content'].strip()
    logging.error('API request failed with status code: {}'.format(response.status_code))
    return None

def clean_filename(filename):
    filename = re.sub('[^\w\s-]', '', filename).strip()
    filename = re.sub('[-\s]+', '-', filename)
    return filename

def process_pdfs(input_directory, output_directory):
    pathlist = Path(input_directory).glob('**/*.pdf')
    for path in pathlist:
        path_in_str = str(path)
        logging.info(f"Processing {path_in_str}")
        try:
            text = extract_first_page_text(path_in_str)
            raw_filename = generate_filename(text)
            if raw_filename:
                clean_file = clean_filename(raw_filename)
                filename = f"{clean_file}.pdf"
                i = 1
                while os.path.exists(os.path.join(output_directory, filename)):
                    filename = f"{clean_file}_{i}.pdf"
                    i += 1
                os.rename(path_in_str, os.path.join(output_directory, filename))
                logging.info(f"Renamed to {filename}")
            else:
                logging.error('Failed to generate filename for {}'.format(path_in_str))
        except Exception as e:
            logging.error(f"Error occurred with file {path_in_str}: {str(e)}")

input_directory = input("Please enter the path to the directory with PDF files: ")
output_directory = input("Please enter the path to the directory to save renamed files (leave blank to use the same as input directory): ")
if not output_directory:
    output_directory = input_directory
process_pdfs(input_directory, output_directory)
