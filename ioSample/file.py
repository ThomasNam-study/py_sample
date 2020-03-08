f = open('listTest.py', 'r')

content = f.read()

print(content)

f.close()

with open('listTest.py', 'r') as f:
    line = f.readline()

    while line:
        print(line, end='###\n')
        line = f.readline()
