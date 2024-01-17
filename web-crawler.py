import sys
import os
import re
import logging
import remote_files
import html_parser
from pathlib import Path

def get_file_path_from_url(url):
    path_no_protocol = re.sub(".*://", "", url)
    if(path_no_protocol.endswith("/")):
        path_no_protocol = path_no_protocol + "index.html"
    return os.path.normpath(path_no_protocol)

def save_file_to_disk(base_url, response_body):
    file_path = get_file_path_from_url(base_url)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as file:
        file.write(response_body)


# -----------------------------------------------

urlsCrawled = []

base_url = str(sys.argv[1])
logging.basicConfig(level=logging.INFO)

response_body = remote_files.download_file_and_return_bytes(base_url)
save_file_to_disk(base_url, response_body)
urlsCrawled.append(base_url)

links = html_parser.find_linked_references(str(response_body))