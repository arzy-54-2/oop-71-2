# Родительский|Супер класс
class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        return f"{self.name} действие!sds"

# ardager = Hero("Ardager", 1000, 10)
# kirito = Hero("Kirito", 111, 11)

# Наследование

# Дочерний класс
class MageHero(Hero):

    def __init__(self, name, hp, lvl, mp):
        super().__init__(name, hp, lvl)
        self.mp = mp

    def action(self):
        return f"This my base action {self.name}"

    def cast_spell(self):
        self.mp -= 1
        return f"{self.name} cast fire bool!!"

asuna = MageHero("Asuna", 122, 12, 1000)

print(type(asuna))
# print(type(kirito))
print(asuna.mp)
print(asuna.cast_spell())
print(asuna.mp)




class Fly:
    def fly(self):
        print("Fly")

class Swim:
    def swim(self):
        print('Swim')

class Duck(Fly, Swim):
    pass

donald_duck = Duck()

# donald_duck.swim()
# donald_duck.fly()


class A:
    def action(self):
        super().action()
        print("A")
class C(A):
    def action(self):
        super().action()
        print('C')
class B(A):
    def action(self):
        super().action()
        print("B")
class D(C,B):
    def action(self):
        super().action()
        print("D")

test_obj = D()
# print(D.__mro__)
# test_obj.action()

