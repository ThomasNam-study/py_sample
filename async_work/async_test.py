async def f():
    return 123

print(type(f))

import inspect

# 코루틴 함수를 알아낼수 있다.
print(inspect.iscoroutinefunction(f))

# 코루틴을 생성한다.
coro = f()
print(type(coro))       # <class 'coroutine'>
print(inspect.iscoroutine(coro))    # True

try:
    coro.send(None)
except StopIteration as e:
    print('The answer was: ', e.value)