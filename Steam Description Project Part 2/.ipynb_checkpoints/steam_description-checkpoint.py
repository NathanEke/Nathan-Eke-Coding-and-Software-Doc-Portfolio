# ------------------------------------------------------------
# Source https://playwright.dev/python/docs/
# ------------------------------------------------------------

from playwright.sync_api import sync_playwright, Playwright

import pathlib
import urllib.request
from bs4 import BeautifulSoup as bs
import os, sys
import time 

import pathlib
from bs4 import BeautifulSoup as bs

toc_folder = pathlib.Path("TOCs")
toc_files = toc_folder.glob("*.html")

def getURLs(genre):

    list_of_urls = []

    fpath = toc_folder / f"{genre}.html"
    print(fpath)

    fin = open(fpath, errors="ignore")
    html_str = fin.read()
    fin.close()

    soup = bs(html_str, "html.parser")           # create a beautifulsoup object
    divs = soup.find_all('div', { 'class' : 'ImpressionTrackedElement' })  # find the div tag, where class = content.

    for div in divs:
        atag =  div.find('a')
        if atag is not None:
            url = atag.get('href', None)
            list_of_urls.append(url)
    else:
        print("Error")

    print(f"{len(list_of_urls)} urls found.")

    return list_of_urls

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'}

html_folder = pathlib.Path("html")

def run(playwright: Playwright, genre):

    list_of_urls = getURLs(genre)

    genre_html_folder = html_folder / genre

    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.set_extra_http_headers(headers)

    for url in list_of_urls:
        print("URL       :",url)      
        page.goto(url)
        page.wait_for_load_state() 

        time.sleep(1)
        html_str = page.content()                                   # Retrieve the HTML Content

        url_path = pathlib.Path(url)
        stem = url_path.stem
        filename = stem[:stem.rfind('?')]
        fpath = genre_html_folder / f"{filename}.html"
        print("Local Path:", fpath)
        print("---")

        fout = open(fpath, 'w')      
        fout.write(html_str)
        fout.close()        

def main(argv):
    bTest = False

    if len(argv) == 4:
        print("python steam_description.py <genre>")

    genre = argv[0];

    with sync_playwright() as playwright:
        run(playwright, genre)

if __name__ == '__main__':
    main(sys.argv[1:])




