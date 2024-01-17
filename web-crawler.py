import sys
import requests
import logging
import re

baseUrl = str(sys.argv[1])

logging.basicConfig(level=logging.INFO)

# Get the base page to start the crawl
logging.info(f"Getting base page from {baseUrl}")
try:
    response = requests.get(baseUrl)
    responseCode = response.status_code
    if responseCode != 200:
        logging.fatal(f"Unable to get response from base URL.  Response code was {responseCode}")
        exit()

    responseBody = str(response.content)
    logging.debug(responseBody)

except:
    logging.fatal(f"Unable to get response from base URL due to failure")
    exit()
    
# Search the response to find page, script, img and css references
scriptSources = re.findall("\\<script\\s.*?\\s?src=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", responseBody, re.MULTILINE)
print(f"Scripts: {scriptSources}")

linkSources = re.findall("\\<link\\s.*?\\s?href=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", responseBody)
print(f"Links: {linkSources}")

imgSources = re.findall("\\<img\\s.*?\\s?src=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", responseBody)
print(f"Images: {imgSources}")

aSources = re.findall("\\<a\\s.*?\\s?href=\"([a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)\"", responseBody)
print(f"As: {aSources}")