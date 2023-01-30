import gdown
import os
import shutil
import zipfile

def download_dataset():
    # Download data from Google Drive
    url = "https://drive.google.com/uc?id=1NFlNvsjzBUh_7oqU0tHz9bvVtcyMk-TC"
    output = "xray_pneumonia_train.zip"
    gdown.download(url, output, quiet=False)

    # Extract downloaded data
    directory_to_extract_to = "./data/"
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

    # Delete _MACOSX directory
    shutil.rmtree("./data/__MACOSX")

    # Delete downloaded zip data file
    os.remove(output)


if __name__ == '__main__':
    if not os.path.isdir("./data/train/"):
        download_dataset()