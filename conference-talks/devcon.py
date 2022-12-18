"""
Crawls presentations from devcon.

Reading is faster than listening.
"""
import requests
import hashlib
import os
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
from tqdm import tqdm

def crawl(link):
    file_path = hashlib.sha256(link.encode()).hexdigest()
    html_path = os.path.join(
        os.path.dirname(__file__),
        ".html"
    )
    os.makedirs(html_path, exist_ok=True)
    html_path = os.path.join(
        html_path,
        file_path
    )
    html = None
    if os.path.isfile(html_path):
        with open(html_path, "r") as file:
            html = file.read() 
    else:
        html = requests.get(link).text
        with open(html_path, "w") as file:
            file.write(html)

    soup = BeautifulSoup(html, 'html.parser')

    return soup

def get_base_name(url):
    a = urllib.parse.urlparse(url)
    return os.path.basename(a.path)

def get_talks():
    link = "https://archive.devcon.org/archive/playlists/devcon-6/"
    soup = crawl(link)
    cards = soup.find_all("a", href=lambda x: "/archive/watch/6/" in x)
    talks = list(map(lambda x: urllib.parse.urljoin(link, x["href"]), cards))

    return talks

def get_presentation(link):
    soup = crawl(link)
    slides_link = soup.find("a", href=lambda x: ".pdf" in x and "resources" in x)
    if slides_link is not None:
        slides_link = slides_link["href"]
        slides_link = urllib.parse.urljoin(link, slides_link)

        slides_path = os.path.join(
            os.path.dirname(__file__),
            "slides"
        )
        os.makedirs(slides_path, exist_ok=True)
        slides_path = os.path.join(
            slides_path,
            get_base_name(slides_link)
        )
        if os.path.isfile(slides_path):
            return None

        response = requests.get(slides_link, stream=True)
        with open(slides_path, "wb") as file:
            for data in tqdm(response.iter_content()):
                file.write(data)

for i in get_talks():
    get_presentation(i)



