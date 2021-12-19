class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.position} {self.name} {self.surname}"


    def get_total_income(self):
        return f"Зарплата: {self._income['wage'] + self._income['bonus']} руб."


person_1 = Position('Василий', 'Петров', 'Уборщик', 15000, 10000)
print(person_1.get_full_name())
print(person_1.get_total_income())