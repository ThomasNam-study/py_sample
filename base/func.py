# args 는 튜플 형태
# kwargs 는 dict 형태로 수신
def args_func(*args, **kwargs):
    for i, v in enumerate(args):
        print(i, v)

    print(kwargs)


def nested_func(num):
    def func_in_func(num):
        print(num)

    print("in func")
    func_in_func((num + 10000))


args_func('kim')
args_func('kim', 'park')
args_func('kim', 'park', 'lee')
args_func('kim', 'park', 'lee', test="우하하")

nested_func(10000)

lambda_func = lambda x: x * 10
print(">>>", lambda_func(10))
