# SplitPDF

## Description
This Python script splits a PDF file into separate pages based on the specified page numbers and generates a new PDF file containing only the selected pages. It utilizes the PyPDF2 library for reading and writing PDF files.

## Features
- Split a PDF file into separate pages.
- Choose specific page numbers to include in the output PDF.
- Simple and straightforward implementation.

## Requirements
- PyPDF2 library (install using `pip install PyPDF2`)

## Usage
1. Update the `pdf_file_path` variable with the path to the PDF file you want to split.
2. Modify the `pages` list to include the page numbers you want to extract. The page numbers should be zero-based (e.g., 0 for the first page).
3. Run the Python script.
4. The script will generate a new PDF file named 'output.pdf' containing the selected pages from the input PDF file.
5. Check the console output for confirmation.

## Important Notes
- Ensure that the specified PDF file exists at the provided file path.
- Page numbers in the `pages` list should be within the range of available pages in the PDF file. Otherwise, it will raise an IndexError.
- The output PDF file will contain only the selected pages in the order specified in the `pages` list.
- This script does not modify the original PDF file; it creates a new file with the selected pages.

## Files
- `SplitPDF.py`: The main Python script.
- 'File 1.pf'
- `README.md`: This file providing information about the script.
