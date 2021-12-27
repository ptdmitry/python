class OfficeEquipmentStock:
    def __init__(self, model, price, count):
        self.model = model
        self.price = price
        self.count = count
        self.stock = []
        self.technics = {}

    def acceptance(self):
        try:
            equipment = input("Введите наменование оборудования: ")
            equipment_price = int(input("Введите цену: "))
            equipment_count = int(input("Введите количество: "))
            accept = {"Модель": equipment, "Цена": equipment_price, "Количество": equipment_count}
            self.stock.append(accept)
            print(self.stock)
            print(f'Продолжить? Да - "y", Нет "n"')
            quit_accept = input(" ")
            if quit_accept == "n":
                print(f"Склад: {self.stock}")
            elif quit_accept == "y":
                return OfficeEquipmentStock.acceptance(self)
            else:
                print("Выход")
        except:
            print(f"Ошибка ввода. Введено не число. Склад: {self.stock}")
            return OfficeEquipmentStock.acceptance(self)


class Laptop(OfficeEquipmentStock):
    def to_work(self):
        return f"Ноутбук: {self.model}. Цена: {self.price} руб. Количество: {self.count} шт."


class Printer(OfficeEquipmentStock):
    def to_print(self):
        return f"Принтер: {self.model}. Цена: {self.price} руб. Количество: {self.count} шт."


class Scaner(OfficeEquipmentStock):
    def to_scan(self):
        return f"Сканер: {self.model}. Цена: {self.price} руб. Количество: {self.count} шт."


a = OfficeEquipmentStock(1, 2, 3)
a.acceptance()
