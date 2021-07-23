import asyncio
from asyncio import Future


async def main(f: Future):
    await asyncio.sleep(1)

    f.set_result('I have finished.')


loop = asyncio.get_event_loop()

f = Future()
print(f.done())

loop.create_task(main(f))

result = loop.run_until_complete(f)

print(result)
print(f.done())
print(f.result())