import pytest
import pdfplumber

from main import process_text_with_columns, detect_barcodes, extract_pdf_info


@pytest.fixture
def test_pdf():
    return "path/to/test_task.pdf"


def test_process_text_with_columns(test_pdf):
    with pdfplumber.open(test_pdf) as pdf:
        page = pdf.pages[0]
        barcodes = detect_barcodes(page)
        processed_text = process_text_with_columns(page, barcodes)

        # Checking if the processed text matches expected structure
        assert 'line_1' in processed_text
        assert 'header' in processed_text['line_1']
        assert len(processed_text['line_1']['header']) > 0
        assert isinstance(processed_text['line_2'], str) and processed_text['line_2'] == 'barcode'
        assert 'PN' in processed_text['line_4']['column_1'] and 'SN' in processed_text['line_4']['column_2']
        assert 'DESCRIPTION' in processed_text['line_5']['column_1']
        assert 'LOCATION' in processed_text['line_6']['column_1'] and 'CONDITION' in processed_text['line_6']['column_2']
        assert 'RECEIVER' in processed_text['line_7']['column_1'] and 'UOM' in processed_text['line_7']['column_2']
        assert 'EXP DATE' in processed_text['line_8']['column_1'] and 'PO' in processed_text['line_8']['column_2']
        assert 'CERT SOURCE' in processed_text['line_9']['column_1']
        assert 'REC.DATE' in processed_text['line_10']['column_1'] and 'MFG' in processed_text['line_10']['column_2']
        assert 'BATCH' in processed_text['line_11']['column_1'] and 'DOM' in processed_text['line_11']['column_2']
        assert 'REMARK' in processed_text['line_12']['column_1'] and 'LOT' in processed_text['line_12']['column_2']
        assert 'TAGGED BY' in processed_text['line_13']['column_1'] and 'NOTES' in processed_text['line_13']['column_2']
        assert isinstance(processed_text['line_14'], str) and processed_text['line_14'] == 'barcode'
        assert 'inspection notes' in processed_text['line_15']['column_2']
        assert 'Qty' in processed_text['line_16']['column_1']



def test_detect_barcodes(test_pdf):
    with pdfplumber.open(test_pdf) as pdf:
        page = pdf.pages[0]
        barcodes = detect_barcodes(page)

        # Checking if barcodes are detected correctly
        assert isinstance(barcodes, list)
        for barcode in barcodes:
            assert 'text' in barcode and barcode['text'] == 'barcode'
            assert 'x0' in barcode and 'top' in barcode



def test_extract_pdf_info(test_pdf):
    pdf_info = extract_pdf_info(test_pdf)

    # Checking if the extracted PDF info matches expected structure
    assert 'metadata' in pdf_info
    assert 'pages' in pdf_info
    for page in pdf_info['pages']:
        assert 'page_number' in page
        assert 'text' in page


if __name__ == '__main__':
    pytest.main()