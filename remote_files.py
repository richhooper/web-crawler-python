# Get the base page to start the crawl
import requests
import logging

def download_file_and_return_bytes(url):
    logging.info(f"Getting base page from {url}")
    try:
        response = requests.get(url)
        response_code = response.status_code
        if response_code != 200:
            logging.fatal(f"Unable to get response from URL.  Response code was {response_code}")
            return ""

        response_body = response.content

    except:
        logging.fatal("Unable to get response from URL due to failure")
        raise

    return response_body