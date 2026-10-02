# class BankAccount:
#
#     def __init__(self, login, password, balance):
#         self.login = login
#         self.__password = password
#         self._balance = balance
#
#     def get_balance(self, user_pass):
#         if user_pass == self.__password:
#             return self._balance
#         return "неверный пароль!!"
#
#     def __reset_pass(self):
#         self.__password = "1234"
#         return "аш пароль теперь 1234"
#
#     def new_pass(self, old_pass):
#         if self.__password == old_pass:
#             return self.__reset_pass()
#         return "неверный старый пароль!!"
#
#
# ardager = BankAccount("ardager_dev", "2233", 1000)
# # print(ardager._BankAccount__password)
# # print(dir(ardager))
# # print(ardager.login)
# # print(ardager.get_balance("2233"))
# # print(ardager.new_pass("223s3"))
# # print(ardager.get_balance())
# # print(ardager._balance)
#
from abc import ABC, abstractmethod
#
# # Абстрактный класс
# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#     @abstractmethod
#     def voce(self):
#         pass
#
# class Dog(Animal):
#     def move(self):
#         print("Step")
#     def voce(self):
#         print("Gaf GAf")
#
# class Cat(Animal):
#     def move(self):
#         print("Step")
#     def voce(self):
#         print("May AMy")
#
# gufi = Dog()
# kiti = Cat()
# gufi.voce()
# kiti.voce()

class SendOTP(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass
class KgOTP(SendOTP):
    def send_otp(self, phone):
        data = f'''
            <Phone>{phone}</Phone>
            <Text>Ваш код :1234</Text>
        '''
        return data
class RuOTP(SendOTP):
    def send_otp(self, phone):
        data = {
            "phone": phone,
            "text": 'Ваш код :1234'
        }
        return data