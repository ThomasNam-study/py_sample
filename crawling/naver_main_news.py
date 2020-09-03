import requests
import lxml.html


def scrape_news_list_page(response):
    urls = []
    root = lxml.html.fromstring(response.content)

    for a in root.cssselect('._NM_UI_PAGE_CONTAINER'):
        print(a)

    return urls

def main():

    response = requests.get('https://www.naver.com')

    urls = scrape_news_list_page(response)

    for url in urls:
        print(url)


if __name__ == "__main__":
    main()