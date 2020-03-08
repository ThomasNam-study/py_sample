import re
import time
import pymongo

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def make_links_absolute(soup, url):
    for tag in soup.findAll('a', href=True):
        tag['href'] = urljoin(url, tag['href'])

def scrape_list_page(r):
    # 파서 생성
    soup = BeautifulSoup(r.text, 'html.parser')

    make_links_absolute(soup, 'http://www.hanbit.co.kr')

    for a in soup.select('.view_box .book_tit a'):
        url = a.get("href")
        yield url

def scrape_detail_page(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    ebook = {
        'url': response.url,
        'title': soup.select_one('.store_product_info_box h3').string,
        'price': soup.select_one('.pbr strong').string,
        'key': extract_key(response.url),
        'content': [normalize_space(p.string) for p in soup.select('#tabs_3 .hanbit_edit_view p') if normalize_space(p.string) != '']
    }

    return ebook

def normalize_space(s):
    if not s:
        return ""

    return re.sub('\\s+', ' ', s).strip()

def extract_key(url):
    m = re.search(r"p_code=(.+)", url)

    return m.group(1)

def main():
    client = pymongo.MongoClient('localhost', 27017)

    collection = client.scraping.ebooks

    collection.create_index('key', unique=True)

    session = requests.Session()
    r = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')

    urls = scrape_list_page(r)

    for url in urls:
        time.sleep(1)
        r = session.get(url)

        key = extract_key(url)
        ebook = collection.find_one({'key': key})

        if not ebook:
            ebook = scrape_detail_page(r)

            collection.insert_one(ebook)

        print(ebook)

    client.close()

if __name__ == '__main__':
    main()
