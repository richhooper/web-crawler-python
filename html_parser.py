import re
from dataclasses import dataclass

@dataclass
class FileReferences:
    scripts: []
    links: []
    images: []
    hyperlinks: []

def find_linked_references(file_body):

    body_string = file_body
    
    # Search the body to find page, script, img and css references
    script_sources = re.findall("\\<script\\s.*?\\s?src=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", body_string)

    link_sources = re.findall("\\<link\\s.*?\\s?href=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", body_string)

    img_sources = re.findall("\\<img\\s.*?\\s?src=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", body_string)

    a_sources = re.findall("\\<a\\s.*?\\s?href=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", body_string)

    return FileReferences(script_sources, link_sources, img_sources, a_sources)