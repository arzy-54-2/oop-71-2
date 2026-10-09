from os import name


class Test:
    # Атрибута класса
    name_class = "НАзвание класса TEST"

    def __init__(self, balance, bonus, password):
        # Атрибуты объекта класса
        self.balance = balance
        self.bonus = bonus
        self.__password = password

    def get_value(self):
        return self.bonus

    @staticmethod
    def get_sum_to_int(a, b):
        return a + b

    @classmethod
    def get_class_name(cls):
        return cls.name_class

    @property
    def total_balance(self):
        return self.balance + self.bonus

    @property
    def get_password(self):
        return self.__password

    @get_password.setter
    def get_password(self, value):
        self.__password = value


obj_1 = Test(100,50, "def2638")
obj_2 = Test(200, 50, "def2638")
obj_3 = Test(200, 50, "def2638")
# test = 3
# test_1 = 3
# test_2 = [3]
# test_3 = [3]
# print(Test.get_sum_to_int(4, 12))
# print(obj_1.bonus)
# print(obj_1.total_balance)
# print(obj_1.balance)
# print(Test.get_class_name())
# print(obj_1.balance)
# obj_1.balance = 999
# print(obj_1.balance)
# # print(obj_1.get_password)
# print(obj_1._Test__password)
# obj_1.get_password = "new pass"
# print(obj_1._Test__password)

# abstractmethod
# property
# name.setter
# static
# class

def simple_decorator(func):
    def wrapper(n):
        print("До выполнения")
        func(n)
        print("после выполнения")
    return wrapper

@simple_decorator
def test():
    print("Hello")

# test = simple_decorator(test)
# test()

# Название + func decorator
def greeting_decorator(func):
    def wrapper(name):
        print(f"{name} hello")
        func(name)
    return wrapper

@greeting_decorator
def greet(name):
    print(f"{name} How are you?")

# greet("Ardager")

# Название
@simple_decorator
def repeat_decorator(value):
    # func decorator
    def decorator(func):
        # Обертка для логики
        def wrapper(name):
            for i in range(value):
                func(name)
        return wrapper
    return decorator

@repeat_decorator(4)
def say_hello(name):
    print(f"{name} hello")

say_hello("Ardager")




def class_decorator(cls):
    class NewClass(cls):
        def action(self):
            print("I'm new method!!")
    return NewClass

@class_decorator
class OldClass:
    def action(self):
        print("I'm old method!!")

# obj_7 = OldClass()
#
# obj_7.action()

TEST_1 = 123

TEST_1.__repr__()



