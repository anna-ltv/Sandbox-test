import pdfplumber
import PyPDF2
from pyzbar.pyzbar import decode
from PIL import Image
import io


def process_text_with_columns(page, barcodes):
    text_blocks = page.extract_words()
    processed_text = {}

    # Determine the median coordinate to separate columns
    x_median = (page.bbox[2] - page.bbox[0]) / 2

    prev_bottom = None
    line_number = 1
    column_data = {'column_1': '', 'column_2': ''}

    # Combine text blocks and barcodes, then sort by top coordinate
    all_blocks = sorted(text_blocks + barcodes, key=lambda b: b['top'])

    for block in all_blocks:
        if 'text' in block and block['text'] != 'barcode':
            # Extracting the header line
            if line_number == 1:
                if prev_bottom is not None and block['top'] - prev_bottom > 3:
                    processed_text[f'line_{line_number}'] = {'header': column_data['column_1'] + column_data['column_2']}
                    line_number += 1
                    column_data = {'column_1': '', 'column_2': ''}

                # Add all text to the header line
                column_data['column_1'] += block['text'] + ' '
            else:
                if prev_bottom is not None and block['top'] - prev_bottom > 3:
                    processed_text[f'line_{line_number}'] = column_data
                    line_number += 1
                    column_data = {'column_1': '', 'column_2': ''}

                # Determine if the block belongs to column 1 or column 2
                if block['x0'] < x_median:
                    column_data['column_1'] += block['text'] + ' '
                else:
                    column_data['column_2'] += block['text'] + ' '

            prev_bottom = block['bottom']
        else:  
            # Extracting barcodes
            if line_number == 1:
                processed_text[f'line_{line_number}'] = {'header': column_data['column_1'] + column_data['column_2']}
                line_number += 1
                column_data = {'column_1': '', 'column_2': ''}

            if prev_bottom is not None and block['top'] - prev_bottom > 3:
                processed_text[f'line_{line_number}'] = column_data
                line_number += 1

            # Add barcode to the current line
            processed_text[f'line_{line_number}'] = 'barcode'
            line_number += 1
            column_data = {'column_1': '', 'column_2': ''}

            prev_bottom = block['bottom']

    # Commit the last line if there is any text left
    if column_data['column_1'].strip() or column_data['column_2'].strip():
        if line_number == 1:
            processed_text[f'line_{line_number}'] = {'header': column_data['column_1'] + column_data['column_2']}
        else:
            processed_text[f'line_{line_number}'] = column_data

    # Strip trailing spaces
    for key in processed_text:
        if 'header' in processed_text[key]:
            processed_text[key]['header'] = processed_text[key]['header'].strip()
        elif isinstance(processed_text[key], dict):
            processed_text[key]['column_1'] = processed_text[key]['column_1'].strip()
            processed_text[key]['column_2'] = processed_text[key]['column_2'].strip()

    return processed_text


def detect_barcodes(page):
    barcodes = []
    # Convert the PDF page to an image
    img = page.to_image()
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    pil_img = Image.open(io.BytesIO(img_byte_arr))

    # Decode barcodes
    decoded_objects = decode(pil_img)
    for obj in decoded_objects:
        barcode_data = {
            'x0': obj.rect.left,
            'top': obj.rect.top,
            'x1': obj.rect.left + obj.rect.width,
            'bottom': obj.rect.top + obj.rect.height,
            'text': 'barcode'
        }
        barcodes.append(barcode_data)

    return barcodes


def extract_pdf_info(file_path):
    pdf_info = {}

    # Extracting metadata from a PDF file
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        pdf_info['metadata'] = reader.metadata

        # Extracting text and other information
    with pdfplumber.open(file_path) as pdf:
        pages = []
        for i, page in enumerate(pdf.pages):
            page_data = {}
            page_data['page_number'] = i + 1

            # Detecting barcodes
            barcodes = detect_barcodes(page)

            # Extracting and processing text with columns
            processed_text = process_text_with_columns(page, barcodes)

            page_data['text'] = processed_text

            pages.append(page_data)

        pdf_info['pages'] = pages

    return pdf_info


file_path = 'path/to/test_task.pdf'
pdf_data = extract_pdf_info(file_path)
print(pdf_data)
