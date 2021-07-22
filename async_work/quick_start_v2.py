import asyncio, time


async def main():
    print(f'{time.ctime()} Hello')

    await asyncio.sleep(1.0)

    print(f'{time.ctime()} Goodbye!')


# 코루틴을 실행하기 위해서 필요한 루프 인스턴스를 생성
# 동일 쓰래드 에서 실행하면 같은 인스턴스를 리턴한다.
loop = asyncio.get_event_loop()

# create_task 를 호출하여 루프에 코루틴을 스케줄링한다.
# 반환하는 task객체를 통해 작업의 상태를 모니터랑 할 수 있다.
# 코루틴 완료 후 값을 얻을 수 있따.
task = loop.create_task(main())

# 절단된 코루틴이 완료될 떄까지 기다린다.
# 스케줄링된 다른 작업들도 같ㅇ ㅣ실행된다.
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)

for t in pending:
    t.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)

# 루프의 모든 대기열을 비우고 익스큐터를 종료시킨다.
loop.close()
