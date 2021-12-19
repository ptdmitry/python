class Stationery:
    def title(self):
        return f"Канцелярские принадлежности"


    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationery):
    def draw(self):
        return f"{Stationery().draw()} ручкой"


class Pencil(Stationery):
    def draw(self):
        return f"{Stationery().draw()} карандашом"


class Handle(Stationery):
    def draw(self):
        return f"{Stationery().draw()} маркером"


print(Stationery().title())
print(Stationery().draw())
print(Pen().draw())
print(Pencil().draw())
print(Handle().draw())