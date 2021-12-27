class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def valid_num_date(obj):
        if 0 < obj.day <= 30:
            if 0 < obj.month <= 12:
                if 0 < obj.year <= 3000:
                    return f"Дата {obj.day}-{obj.month}-{obj.year}"
                else:
                    return f"Неправильно введён год {obj.year}"
            else:
                return f"Неправильно введён месяц {obj.month}"
        else:
            return f"Неправильно введён день {obj.day}"

    @classmethod
    def num_date(cls, data):
        my_date = []
        for i in data.split('-'):
            my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])


date = Date(1, 1, 2022)
print(Date.valid_num_date(date))
print(date.num_date('1-1-2022'))
