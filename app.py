import os
import sys
import time
import re
import html
import bs4
import requests
import json

sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):
    
    def parse_date(description):
        date_pattern = r"(\b\w{3}\s\d{1,2},\s\d{4}\b)"
        matches = re.search(date_pattern, description)

        if matches:
            return matches.group(0)
    
    def get_prediction():
        url = "https://www.metaculus.com/questions/3479/date-weakly-general-ai-is-publicly-known/"
        session = requests.Session()
        retries = 3
        timeout = 10  # Set the desired timeout in seconds

        for i in range(retries):
            try:
                response = session.get(url, timeout=timeout)
                break
            except requests.exceptions.RequestException:
                if i == retries - 1:
                    raise
                time.sleep(1)

        soup = bs4.BeautifulSoup(response.content, "html.parser")
        twitter_meta = soup.find("meta", property="twitter:description")

        if twitter_meta:
            description = twitter_meta["content"]
            return parse_date(description)
        else:
            return "Failed to get the description."
    
    try:
        DATE = get_prediction()
        status = '200 OK'
    except:
        DATE = "Error: Incomplete response!"
        status = '500 Internal Server Error'

    headers = [
        ('Content-Type', 'application/json'),
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', 'GET'),
        ('Access-Control-Allow-Headers', 'Content-Type'),
    ]

    if status == '200 OK':
        response = json.dumps({'date': DATE})
    else:
        response = html.escape(DATE)
        headers[0] = ('Content-Type', 'text/plain')
    
    start_response(status, [('Content-Type', 'text/plain')])
    return [response.encode()]
