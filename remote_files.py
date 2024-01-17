# Get the base page to start the crawl
import requests
import logging

def download_file_and_return_bytes(url):
    logging.info(f"Getting base page from {url}")
    try:
        response = requests.get(url)
        responseCode = response.status_code
        if responseCode != 200:
            logging.fatal(f"Unable to get response from URL.  Response code was {responseCode}")
            return ""

        responseBody = response.content

    except:
        logging.fatal(f"Unable to get response from URL due to failure")
        exit()
    return responseBody