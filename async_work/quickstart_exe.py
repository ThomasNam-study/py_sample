import asyncio, time


async def main():
    print(f'{time.ctime()} Hello')

    await asyncio.sleep(3.0)

    print(f'{time.ctime()} Goodbye!')


def blocking():
    time.sleep(0.5)
    print(f'{time.ctime()} Hello from a thread!')


loop = asyncio.get_event_loop()
task = loop.create_task(main())

loop.run_in_executor(None, blocking)
loop.run_until_complete(task)

loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)

for t in pending:
    t.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)

# 루프의 모든 대기열을 비우고 익스큐터를 종료시킨다.
loop.close()

