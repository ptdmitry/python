"""
Урок 3. Массивы. Кортежи. Множества. Списки.

1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратных каждому из чисел в диапазоне от 2 до 9.
"""

count_natural_numbers = 0

for i in range(2, 100):
    for n in range(2, 9):
        if i % n == 0:
            count_natural_numbers += 1

print(f'Количество чисел кратных каждому из чисел от 2 до 99 в диапазоне от 2 до 9: {count_natural_numbers}')


"""
2. Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй 
массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация 
начинается с нуля), т.к. именно в этих позициях первого массива стоят 
четные числа.
"""

my_list = [45, 5, 3, 8, 4, 6, 43, 44, 8, 22, 27, 30, 1, 2, 6, 10]
index_list = []

for i, value in enumerate(my_list):
    if value % 2 == 0:
        index_list.append(i)

print(index_list)

"""
3. В массиве случайных целых чисел поменять местами 
минимальный и максимальный элементы.
"""

some_list = [23, 4, 65, 23, 67, 94, 92, 3, 23, 34, 5, 56, 68, 56, 6, 5, 45, 36]
# Поменяются местами цифры 94 и 3
print(f'{some_list} Исходный список')

max_num = 0
max_num_index = 0
min_num = 0
min_num_index = 0

for i, val in enumerate(some_list):
    if val == max(some_list):
        max_num = val
        max_num_index = i
    elif val == min(some_list):
        min_num = val
        min_num_index = i

some_list[max_num_index] = min_num
some_list[min_num_index] = max_num

print(f'{some_list} Результирующий список')

"""
4. Определить, какое число в массиве встречается чаще всего.
"""

some_tuple = (23, 4, 65, 23, 67, 94, 92, 3, 34, 34, 23, 34, 5, 56, 68, 56, 6, 6, 6, 6, 5, 45, 34, 36, 23, 34)
often_num = []

for i in some_tuple:
    often_num.append(some_tuple.count(i))
    for n in often_num:
        num_max_index = max(often_num)

print(f'Число {some_tuple[often_num.index(max(often_num))]} встречается {max(often_num)} раз')

"""
5. В массиве найти максимальный отрицательный элемент. 
Вывести на экран его значение и позицию в массиве.
"""

negative_tuple = (23, -4, 65, 23, -67, 94, 92, 3, 34, 34, 23, 34, 5, -56, 68, 56, 6, -6, 5, -45)
max_negtive_num = []

for i, count in enumerate(negative_tuple):
    if 0 > count > min(negative_tuple):
        max_negtive_num.append(count)

print(f'Максимально отрицательное число в массиве: {max(max_negtive_num)}, '
      f'его позиция: {negative_tuple.index(max(max_negtive_num))}')

"""
6. В одномерном массиве найти сумму элементов, находящихся 
между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
"""

num_list = [23, 98, 65, 23, 67, 94, 92, 3, 23, 34, 5, 56, 68, 56, 6, 5, 45, 36]

max_num_index = 0
min_num_index = 0
sum_list = []

for i, number in enumerate(num_list):
    if number == max(num_list):
        max_num_index = i
    elif number == min(num_list):
        min_num_index = i
        for m in range(max_num_index + 1, min_num_index):
            sum_list.append(num_list[m])

print(f'Сумма элементов между максимальным {max(num_list)} и минимальным {min(num_list)} элементами: {sum(sum_list)}')

"""
7. В одномерном массиве целых чисел определить два наименьших 
элемента. Они могут быть как равны между собой (оба являться 
минимальными), так и различаться.
"""

number_list = [23, 98, 65, 23, 67, 94, 92, 3, 23, 34, 5, 56, 68, 56, 6, 5, 2, 36]

fst_index = 0
snd_index = 0

for i in number_list:
    if number_list[fst_index] > i:
        snd_index = fst_index
        fst_index = number_list.index(i)
    elif number_list[snd_index] > i:
        snd_index = number_list.index(i)

print(number_list[fst_index], number_list[snd_index])

"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних 
элементов строк. Программа должна вычислять сумму введенных 
элементов каждой строки и записывать ее в последнюю ячейку строки. 
В конце следует вывести полученную матрицу.
"""

rows = 5
lines = 4
matrix = []
print(f'Заполните матрицу {rows}х{lines}, кроме последних элементов: ')

for m in range(rows):
    print(f'{m+1} строка')
    row = [int(input()), int(input()), int(input())]
    matrix.append(row)
    matrix[m].append(sum(row))

print(f'\nРезультирующая матрица: ')
for n in matrix:
    print(f'{n}')

"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
