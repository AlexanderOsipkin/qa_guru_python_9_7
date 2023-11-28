from pypdf import PdfReader
import zipfile


def test_text_in_pdf_file():
    with zipfile.ZipFile('resources/archive.zip') as zip_file:
        with zip_file.open('tmp/file_pdf.pdf') as pdf:
            reader = PdfReader(pdf)
            text = reader.pages[0].extract_text()
            assert 'pytest Documentation' in text
