def myhello1():
    pass


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = []

for i in range(10):
    b.append(i)

print(b)
print(a)

print(a[0:5])
print(a[1:2])

print(len(a))

c = (1, 2, 3)
c1 = 1, 2, 3

print(c)
print(c1)
print(type(c))

d1, d2, d3 = c
print("{0}, {1}, {2}".format(d1, d2, d3))

d = d1, d2, d3

print(d)

dic = {}
dic['a'] = "b"

print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())

if "b" in dic:
    print("b 있음")
else:
    print("b 없음")

a = [1, 3, 5, 7, 9]

b = [2, 5, 7]

for c in b:
    if a.count(c) > 0:
        a.remove(c)

print(a)
