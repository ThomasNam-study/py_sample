import requests
from lxml.html import fromstring, tostring


def scrape_news_list_page(response):
    urls = {}
    root = fromstring(response.content)

    for a in root.cssselect('._NM_UI_PAGE_CONTAINER .tile_view .thumb_area div.thumb_box'):

        name = ""
        url = ""

        for img in a.cssselect('a.thumb>img'):
            name = img.get('alt')

        for b in a.cssselect('div a.btn_popup[data-clk="logo"]'):
            url = b.get('href')

        if name and url:
            urls[name] = url

    return urls


def main():

    # 세션 사용
    session = requests.session()

    response = session.get('https://www.naver.com')

    urls = scrape_news_list_page(response)

    for name, url in urls.items():
        print(name, url)


if __name__ == "__main__":
    main()
