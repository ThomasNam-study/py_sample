# ZeroDivisionError
# IndexError
# KeyError
# AttributeError
# ValueError
# FileNotFoundError
# TypeError

x = [10, 20, 30]

try:
    dic = {}

    print(dic["test"])
except ValueError as e:
    print("VALUE ERROR")
except Exception as e:
    print("ERROR", e)

try:
    print('Try')
finally:
    print("Ok!!")

try:
    a = 'Kim'

    raise ValueError
except:
    print("Ok!!")
