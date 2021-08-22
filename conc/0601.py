# yield from 사용

t = 'ABCDEF'

# For
for c in t:
    print('EX1-1 - ', c)

print()

# ITer
w = iter(t)

while True:
    try:
        print('EX1-2 - ', next(w))
    except StopIteration:
        break

print()

from collections import abc

# 반복형 확인
print('EX1-3 - ', hasattr(t, '__iter__'))
print('EX1-3 - ', isinstance(t, abc.Iterable))

print()
print()


class WordSplitIter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')

    def __next__(self):
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration()

        self._idx += 1
        return word

    def __iter__(self):
        return self

    def __repr__(self):
        return 'WorldSplit(%s)' % (self._text,)


wi = WordSplitIter('Who says the nights are the sleeping')

print('EX2-1', wi)
print('EX2-1', next(wi))
print('EX2-2', next(wi))
print('EX2-3', next(wi))
print('EX2-4', next(wi))
print('EX2-5', next(wi))
print('EX2-6', next(wi))

print()
print()


class WordGene:
    def __init__(self, text):
        self._text = text.split(' ')

    def __iter__(self):
        for word in self._text:
            yield word

    def __repr__(self):
        return 'WorldSplit(%s)' % (self._text,)


wg = WordGene('Who says the nights are the sleeping')

wi = iter(wg)

print('EX3-1', wi)
print('EX3-1', next(wi))
print('EX3-2', next(wi))
print('EX3-3', next(wi))
print('EX3-4', next(wi))
print('EX3-5', next(wi))
print('EX3-6', next(wi))

print()
print()


def gene_ex1():
    print('start')
    yield 'AAA'
    print('content')
    yield 'BBB'
    print('End')


temp = iter(gene_ex1())

# print("EX4-1", next(temp))
# print("EX4-1", next(temp))
# print("EX4-1", next(temp))

for v in gene_ex1():
    print('EX4-3', v)

temp2 = [x * 3 for x in gene_ex1()]
temp3 = (x * 3 for x in gene_ex1())

print('EX-5', temp2)
print('EX-5', temp3)

for i in temp2:
    print("EX5-2 - ", i)

for i in temp3:
    print("EX5-3 - ", i)

print()
print()

import itertools

gen1 = itertools.count(1, 2.5)

print('EX6-1 -', next(gen1))
print('EX6-1 -', next(gen1))
print('EX6-1 -', next(gen1))

gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print('ex6-5 - ', v)

gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print('EX6-6 - ', v)


gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print('EX6-7', v)

print()
print()

gen5 = itertools.chain('ABCDE', range(1, 11, 2))

gen9 = itertools.groupby('AAABBCCCCDDEE')

for c, gr in gen9:
    print('EX6-12 - ', c, ' : ', list(gr))

