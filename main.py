class Hero:
    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты экземпляра класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def base_action(self):
        return f"{self.name} this my base action!!"


#Объект|Экземпляр на основе класса
ardager = Hero("Aradger", 100, 1000)
kirito = Hero("kirito", 100, 1000)
asuna = Hero("Asuna", 100, 1000)
my_int = 123
my_str = "123"
# print(my_str.capitalize())
# print(asuna.base_action())
# print(type(kirito))
# print(type(my_int))

# MageHero
# mage_hero