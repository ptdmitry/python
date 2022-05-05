"""
Урок 5. Коллекции. Список. Очередь. Словарь

1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия. Программа должна определить среднюю
прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
"""

from collections import OrderedDict

companies = {}
OrderedDict(companies)
companies_profit = []

num_companies = int(input(f'Введите количество предприятий: '))

for i in range(num_companies):
    name_companies = input(f'Введите название предприятия №{i + 1}: ')
    for j in range(1, 5):
        profit = int(input(f'Прибыль за {j} квартал предприятия {name_companies}: '))
        companies_profit.append(profit)
    companies[name_companies] = companies_profit
    companies_profit = []
    i -= 1

average_profit = 0

for i in companies:
    average_profit += sum(companies[i])

count_companies = [i for i in companies]

print(f'Перечень предпприятий и их прибыль по кварталам: {companies}')
print(f'Общая прибыль предприятий: {average_profit}')
print(f'Средняя общая прибыль предприятий: {average_profit / len(count_companies)}')
print(f'Количество предприятий: {len(count_companies)}')

for c in companies:
  if sum(companies[c]) > average_profit / len(count_companies):
    print (f'Прибыль {sum(companies[c])}, выше среднего {average_profit / len(count_companies)} у компании: {c}')
  else:
    print (f'Прибыль {sum(companies[c])}, ниже среднего {average_profit / len(count_companies)} у компании: {c}')

"""
При companies = {'Компания 1': [1000, 15000, 2000, 3200], 'Компания 2': [1500, 3500, 7000, 6500], 'Компания 3': 
[9000, 365, 1400, 2400], 'Компания 4': [2500, 7500, 14000, 390], 'Компания 5': [3600, 5800, 12000, 4000]}

Общая прибыль предприятий: 102655
Средняя общая прибыль предприятий: 20531.0
Количество предприятий: 5
Прибыль 21200, выше среднего 20531.0 у компании: Компания 1
Прибыль 18500, ниже среднего 20531.0 у компании: Компания 2
Прибыль 13165, ниже среднего 20531.0 у компании: Компания 3
Прибыль 24390, выше среднего 20531.0 у компании: Компания 4
Прибыль 25400, выше среднего 20531.0 у компании: Компания 5
"""

"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры 
числа. Например, пользователь ввёл A2 и C4F. 
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из 
примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию 
из модуля collections
"""

from collections import Counter

num_1 = input(f'Введите первое шестнадцетиричное число: ').upper() # A2
num_2 = input(f'Введите второе шестнадцетиричное число: ').upper() # C4F

print(f'1-е число: {list(Counter(num_1).elements())}')
print(f'2-е число: {list(Counter(num_2).elements())}')

c = hex(int(''.join(list(Counter(num_1).elements())), base=16))
d = hex(int(''.join(list(Counter(num_2).elements())), base=16))
sum_num = hex((int(c, base=16) + (int(d, base=16)))).upper()
mult_num = hex((int(c, base=16) * (int(d, base=16)))).upper()

print(f'Сумма чисел: {list(sum_num)[2:]}')
print(f'Произведение чисел: {list(mult_num)[2:]}')
