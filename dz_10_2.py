from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, num):
        self.num = num

    @abstractmethod
    def product(self):
        pass

    def __str__(self):
        return f"Пальто: {self.num/6.5 + 0.5}\nКостюм: {self.num*2 + 0.3}"

    def __add__(self, other):
        return f"{(self.num/6.5 + 0.5 + other.num*2 + 0.3):.2f}"


class Cover(Clothing):
    @property
    def product(self):
        return None

    def __str__(self):
        if self.num <= 0:
            return f"Введите корректные значения"
        else:
            return f"Пальто: {self.num/6.5 + 0.5}"

    def __add__(self, other):
        if self.num <= 0 or other.num <= 0:
            return f"Введите корректные значения"
        else:
            return f"Всего ткани: {(self.num/6.5 + 0.5 + other.num*2 + 0.3):.2f} м"


class Suite(Clothing):
    @property
    def product(self):
        return None

    def __str__(self):
        if self.num <= 0:
            return f"Введите корректные значения"
        else:
            return f"Костюм: {self.num*2 + 0.3} м"

    def __add__(self, other):
        if self.num <= 0 or other.num <= 0:
            return f"Введите корректные значения"
        else:
            return f"{(self.num/6.5 + 0.5 + other.num*2 + 0.3):.2f} м"


cover_1 = Cover(6.5)
print(cover_1)
suite_1 = Suite(1.6)
print(suite_1)
print(cover_1 + suite_1)
