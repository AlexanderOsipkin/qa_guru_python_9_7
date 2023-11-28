import csv
import zipfile
from io import TextIOWrapper


def test_text_in_csv_file():
    with zipfile.ZipFile('resources/archive.zip') as zip_file:
        with zip_file.open('tmp/file_csv.csv') as csv_file:
            csvreader = list(csv.reader(TextIOWrapper(csv_file, 'utf-8-sig')))
            assert 'White' == csvreader[1][0]
