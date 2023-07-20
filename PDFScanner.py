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
API_KEY = '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'  # replace with your OpenAI key

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}',
}

# Set the path for Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # adjust the path accordingly

def extract_first_page_text(pdf_path):
    #... existing code ...

def generate_filename(text):
    #... existing code ...

def clean_filename(filename):
    #... existing code ...

def process_pdfs(input_directory, output_directory, recursive):
    glob_pattern = '**/*.pdf' if recursive else '*.pdf'
    pathlist = Path(input_directory).glob(glob_pattern)
    for path in pathlist:
        #... existing code ...

# Ask user for directories
input_directory = input("Please enter the path to the directory with PDF files: ")
output_directory = input("Please enter the path to the directory to save renamed files (leave blank to use the same as input directory): ")
if not output_directory:
    output_directory = input_directory

# Ask user if they want to search subdirectories
recursive_str = input("Do you want to include subdirectories? (yes/no): ").lower()
recursive = recursive_str.startswith('y')

# Start renaming process
process_pdfs(input_directory, output_directory, recursive)
