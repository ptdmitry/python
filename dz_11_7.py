class ComplexNum:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return self.num_1 + other.num_2

    def __mul__(self, other):
        return self.num_1 * other.num_2


class AddNum(ComplexNum):
    def add_num(self):
        return f"Сумма чисел: {self.num_1 + self.num_2}"


class MulNum(ComplexNum):
    def mul_num(self):
        return f"Произведение чисел: {complex(self.num_1.real * self.num_2.real, self.num_1.imag * self.num_2.imag)}"


sumnum_1 = AddNum(2+2j, 3+3j)
print(sumnum_1.add_num())

nummul_1 = MulNum(3+2j, 3+3j)
print(nummul_1.mul_num())
