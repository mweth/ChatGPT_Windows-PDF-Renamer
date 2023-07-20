# ChatGPT_Windows-PDF-Renamer
A basic script to scan all PDFs in a folder and rename them based on GPT suggestion.

---

# PDF File Renamer

This script is a utility for renaming PDF files based on the content of the first page of the document. It makes use of the OpenAI GPT-3.5 turbo model to generate the new file name.

This tool can be very handy for large numbers of PDF files, and it offers the option to search subdirectories recursively.

## Requirements

- Python 3.7 or newer.
- Tesseract-OCR
- Python packages: pytesseract, PyPDF2, pdf2image, requests

## Installation

Follow these steps to install and use the script:

1. Install Python if it's not already installed. You can download it from the official site: [Python.org](https://www.python.org/)

2. Install Tesseract-OCR. It's an OCR engine that this script uses to extract text from scanned PDFs. Download it from the official GitHub repository: [Tesseract-OCR GitHub](https://github.com/UB-Mannheim/tesseract/wiki). Remember the path where you installed Tesseract, you will need it.
   
4. Install Popplrt
    Download the latest [poppler package](https://github.com/oschwartz10612/poppler-windows/releases/).
    Move the extracted directory to the desired place on your system
    Add the bin/ directory to your [PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) environmental variable.
    Test that all went well by opening cmd and making sure that you can call 'pdftoppm -h'

5. Clone this repository to your local machine or download the Python script file.

6. Open a Command Prompt and navigate to the directory where you saved the script.

7. Install the required Python packages by running the following command: `pip install pytesseract PyPDF2 pdf2image requests`.

8. Open the script in a text editor.

9. Update the following line with the path where you installed Tesseract-OCR:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # adjust the path accordingly
```
8. Update the following line with your OpenAI key:
```python
API_KEY = 'sk-YOURKEY'  # replace with your OpenAI key
```

## Usage

Run the script from a Command Prompt with the command: `python <script_name.py>`

The script will ask for the following input:

- Directory with PDF files: Enter the full path to the directory where your PDF files are located.
- Directory to save renamed files: Enter the full path to the directory where you want to save the renamed files. You can use the same directory as the input directory.
- Include subdirectories: Enter "yes" or "no". If you enter "yes", the script will also rename PDFs found in subdirectories of the input directory.

## Note

Please remember to handle your OpenAI key with care. Don't share it or expose it in public repositories.
