class UserInfo:

    def __init__(self, name):
        self.name = name

    def user_info_p(self):
        print("Name :", self.name)


class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = UserInfo("개똥이")
user1.user_info_p()

user2 = UserInfo("Bob")
user2.user_info_p()

print(id(user1))
print(id(user2))

print(user1.__dict__)
print(user2.__dict__)
