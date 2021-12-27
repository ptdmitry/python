class NumbEx:
    def __init__(self, *args):
        self.lst = []

    def input(self):
        while True:
            try:
                value = int(input("Введите число: "))
                self.lst.append(value)
                print(f"Список чисел: {self.lst}")
            except:
                print(f"Вы ввели не число!")
                question = input("Продолжить? y or n: ")
                if question == "y":
                    print(self.lst)
                else:
                    return f"Ваш список: {self.lst}"


numbers = NumbEx()
print(numbers.input())