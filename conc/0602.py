def coroution1():
    print('>>> coroution started.')
    i = yield
    print(">>> coroution received: {}".format(i))


# c1 = coroution1()
#
# print('EX1-1', c1, type(c1))
# next(c1)
# c1.send(100)

c2 = coroution1()


# GEN_CREATED
def coroutine2(x):
    print('>>> coroutine started: {}'.format(x))
    y = yield x
    print('>>> coroutine received: {}'.format(y))
    z = yield x + y
    print('>>> coroutine received: {}'.format(z))


c3 = coroutine2(10)

from inspect import getgeneratorstate

print('EX1-2 - ', getgeneratorstate(c3))

print(next(c3))

print('EX1-2 - ', getgeneratorstate(c3))
print(c3.send(15))

print('EX1-2 - ', getgeneratorstate(c3))

# print(c3.send(20))

from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@coroutine
def sumer():
    total = 0
    term = 0

    while True:
        term = yield total
        total += term


su = sumer()

print('EX2-1 - ', su.send(100))
print('EX2-1 - ', su.send(40))


class SampleException(Exception):
    pass


def coroutine_except():
    print('>> coroutine started.')

    try:
        while True:
            try:
                x = yield
            except SampleException:
                print(' -> SampleException Handled')
            else:
                print('-> Coroutine received : {}'.format(x))
    finally:
        print('-> coroutine ending')


exe_co = coroutine_except()

print('EX3-1 - ', next(exe_co))
print('EX3-1 - ', exe_co.send(10))
print('EX3-1 - ', exe_co.send(100))
print('EX3-1 - ', exe_co.throw(SampleException))
print('EX3-1 - ', exe_co.send(200))
print('EX3-1 - ', exe_co.close())
# print('EX3-1 - ', exe_co.send(200))

print()
print()


def averager_re():
    total = 0.0
    cnt = 0
    avg = None

    while True:
        term = yield
        if term is None:
            break

        total += term
        cnt += 1
        avg = total / cnt

    return 'Average : {}'.format(avg)


avg2 = averager_re()

next(avg2)

avg2.send(10)
avg2.send(30)
avg2.send(50)

try:
    avg2.send(None)
except StopIteration as e:
    print('EX4-1', e.value)


def gen1():
    for x in 'AB':
        yield x

    for y in range(1, 4):
        yield y


t1 = gen1()

print('EX5-1 - ', next(t1))
print('EX5-2 - ', next(t1))
print('EX5-3 - ', next(t1))
print('EX5-4 - ', next(t1))

t2 = gen1()
print('EX5-7 - ', list(t2))


def gen2():
    yield from 'AB'
    yield from range(1, 4)


t3 = gen2()

print()
print()


def gen3_sub():
    print('Sub coroutine.')

    x = yield 10
    print('Recv 1 : ', str(x))
    y = yield 100
    print('Recv 2 : ', str(x))


def gen4_main():
    yield from gen3_sub()


t5 = gen4_main()
print('EX7-1 - ', next(t5))
print('EX7-1 - ', t5.send(7))
print('EX7-1 - ', t5.send(77))
