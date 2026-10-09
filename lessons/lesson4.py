# # | Метод         | Что делает                |
# # | ------------- | ------------------------- |
# # | `__init__`    | конструктор               |
# # | `__str__`     | вывод через `print()`     |
# # | `__repr__`    | отображение объекта       |
# # | `__len__`     | `len(obj)`                |
# # | `__getitem__` | `obj[key]`                |
# # | `__call__`    | вызов объекта как функции |
# # | `__eq__`      | `==`                      |
# # | `__lt__`      | `<`                       |
# # | `__gt__`      | `>`                       |
#
#
# # | Оператор | Магический метод | Пример   |
# # | -------- | ---------------- | -------- |
# # | `+`      | `__add__`        | `a + b`  |
# # | `-`      | `__sub__`        | `a - b`  |
# # | `*`      | `__mul__`        | `a * b`  |
# # | `/`      | `__truediv__`    | `a / b`  |
# # | `//`     | `__floordiv__`   | `a // b` |
# # | `%`      | `__mod__`        | `a % b`  |
#
# class Test:
#     def __init__(self, value):
#         # Атрибуты объекта класса
#         self.value = value
#     # print()
#     def __str__(self):
#         return f"{self.value}"
#
#     # +
#     def __add__(self, other):
#         print(self.value)
#         print(other.value)
#         # return self.value + other.value
#
# obj_1 = Test(123)
# obj_2 = Test(321)
#
# my_int = int(123)
# my_int_2 = int(321)
#
# data_1 = my_int * my_int_2
# print(data_1)
#
#
# data_2 = obj_2 + obj_1
# print(data_2)
#
# # print(obj_1)
# # print(my_int)
#


class Money:
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def __converter(self, money):
        pass

    def __add__(self, other):
        if self.currency == other.currency:
            return self.value + other.value
        else:
            raise ValueError("Валюты разные!!")

m_bank = Money(100, "usd")
kompanion = Money(100, "som")

# data = m_bank + kompanion

class Video:

    def __init__(self, title, description, view_count=0):
        self.title = title
        self.description = description
        self.view_count = view_count

    def __call__(self, other):
        self.view_count += 1
        if type(self.title) == type(other.title):
            pass


video_1 = Video(m_bank, "new song")
video_2 = Video(kompanion, "Опенинг Наруто")

print(video_2.title.currency)
