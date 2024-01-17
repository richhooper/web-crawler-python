import re
from dataclasses import dataclass

@dataclass
class FileReferences:
    scripts: []
    links: []
    images: []
    hyperlinks: []

def find_linked_references(fileBody):

    bodyString = fileBody
    
    # Search the body to find page, script, img and css references
    scriptSources = re.findall("\\<script\\s.*?\\s?src=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", bodyString)

    linkSources = re.findall("\\<link\\s.*?\\s?href=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", bodyString)

    imgSources = re.findall("\\<img\\s.*?\\s?src=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", bodyString)

    aSources = re.findall("\\<a\\s.*?\\s?href=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", bodyString)

    return FileReferences(scriptSources, linkSources, imgSources, aSources)