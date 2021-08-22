import threading
import timeit
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import asyncio

urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://github.com/',
        'https://gmarket.co.kr/']

start = timeit.default_timer()


async def fetch(url, executor):
    print('Thread Name :', threading.current_thread().getName(), 'Start', url)

    res = await loop.run_in_executor(executor, urlopen(url))
    print('Thread Name :', threading.current_thread().getName(), 'Done', url)

    return res.read()[0:5]


async def main():
    executor = ThreadPoolExecutor(max_workers=10)
    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]

    rst = await asyncio.gather(*futures)

    print()
    print('Result : ', rst)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main())

    # main()
    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print('Total Time : ', duration)
