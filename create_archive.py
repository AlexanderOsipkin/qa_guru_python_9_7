import zipfile
import os
from script_os import TMP_DIR
from script_os import RESOURCES_DIR


def test_create_archive():
    files = os.listdir(TMP_DIR)
    archive = os.path.join(RESOURCES_DIR, 'archive.zip')

    with zipfile.ZipFile(archive, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        for file in files:
            add_file = os.path.join("tmp", file)
            zf.write(add_file)
