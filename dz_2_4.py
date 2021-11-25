staff = ['инженер-конструктор Игорь',
         'главный бухгалтер МАРИНА',
         'токарь высшего разряда нИКОЛАй',
         'директор аэлита']

for ind in range(len(staff)):
    name = ''.join(staff[ind].split(' ')[-1])
    print(f'Привет {name.title()}')