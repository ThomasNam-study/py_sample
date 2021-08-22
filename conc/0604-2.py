import threading
import timeit
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen

urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://github.com/',
        'https://gmarket.co.kr/']

start = timeit.default_timer()


def fetch(url):
    print('Thread Name :', threading.current_thread().getName(), 'Start', url)
    urlopen(url)
    print('Thread Name :', threading.current_thread().getName(), 'Done', url)


def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            executor.submit(fetch, url)


if __name__ == '__main__':
    main()
    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print('Total Time : ', duration)
