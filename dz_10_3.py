class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"{self.num}"

    def __add__(self, other):
        return Cell('*' * (self.num + other.num))

    def __sub__(self, other):
        if self.num > other.num:
            return Cell('*' * (self.num - other.num))
        else:
            return f"Первое число меньше второго"

    def __mul__(self, other):
        return Cell('*' * self.num * other.num)

    def __truediv__(self, other):
        return Cell('*' * round(self.num/other.num))

    def make_order(self, row):
        return '\n'.join(['*' * row for _ in range(self.num // row)]) + '\n' + '*' *\
                             (self.num % row)


num_1 = Cell(10)
num_2 = Cell(5)

print(num_1 + num_2, end='\n')
print(num_1 - num_2, end='\n')
print(num_1 * num_2, end='\n')
print(num_1 / num_2, end='\n')
print(num_1.make_order(4))
