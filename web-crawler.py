import sys
import os
import re
import logging
import remote_files
import html_parser
from pathlib import Path

def get_file_path_from_url(url):
    pathNoProtocol = re.sub(".*://", "", url)
    if(pathNoProtocol.endswith("/")):
        pathNoProtocol = pathNoProtocol + "index.html"
    return os.path.normpath(pathNoProtocol)

def save_file_to_disk(baseUrl, responseBody):
    filePath = get_file_path_from_url(baseUrl)
    os.makedirs(os.path.dirname(filePath), exist_ok=True)

    with open(filePath, "wb") as file:
        file.write(responseBody)

# -----------------------------------------------

urlsCrawled = []

baseUrl = str(sys.argv[1])
logging.basicConfig(level=logging.INFO)

responseBody = remote_files.download_file_and_return_bytes(baseUrl)
save_file_to_disk(baseUrl, responseBody)
urlsCrawled.append(baseUrl)

links = html_parser.find_linked_references(str(responseBody))