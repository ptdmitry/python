"""
Урок 4. Эмпирическая оценка алгоритмов на Python

1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Задача. В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

# Вариант 1:

from random import randint

import time

num_list = [randint(1, 100) for i in range(10000)]

start = time.time()

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

finish = time.time()

print(f'Сумма элементов между максимальным {max(num_list)} и минимальным {min(num_list)} элементами: {sum(sum_list)}')

print(finish - start, 'с')
print('Сложность алгоритма: O(n)')
print()

# Вариант 2:

from random import random
import time

N = 10000
a = [0]*N
for i in range(N):
    a[i] = int(random()*100)

start = time.time()

min_id = 0
max_id = 0
for i in range(1, N):
    if a[i] < a[min_id]:
        min_id = i
    elif a[i] > a[max_id]:
        max_id = i

if min_id > max_id:
    min_id, max_id = max_id, min_id

summa = 0
for i in range(min_id+1, max_id):
    summa += a[i]

finish = time.time()

print(finish - start, 'с')
print(f"Сумма чисел {summa}")
print()

# Вариант 3:

import random

r = [random.randint(0, 99) for _ in range(10000)]

min_index = 0
max_index = 0
step = 1
sum = 0

start = time.time()

for i in r:
    if r[min_index] > i:
        min_index = r.index(i)
    elif r[max_index] < i:
        max_index = r.index(i)

if max_index - min_index < 0:
    step = -1

for i in r[min_index + step:max_index:step]:
    sum += i

finish = time.time()

print(finish - start, 'с')
print(f'Сумма элементов между минимальным ({r[min_index]}), '
      f'и максимальным ({r[max_index]}) элементами: {sum}')

"""
Результаты:

Вариант 1:
Сумма элементов между максимальным 100 и минимальным 1 элементами: 571127
3.276244878768921 с
Сложность алгоритма: O(n)

Вариант 2:
0.0010366439819335938 с
Сумма чисел 1058

Вариант 3:
0.0 с
Сумма элементов между минимальным (0)  и максимальным (99) элементами: 1277
"""
# ---------------------------------------------------------------------------------------------------
"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость 
и сложность алгоритмов. Результаты анализа сохранить в виде комментариев 
в файле с кодом.
"""

# Вариант 1. Без использования «Решета Эратосфена»

import time

print('Без использования «Решета Эратосфена»')
simple_numbers = []

start = time.time()


def test(num, n=10000):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(f'Количество простых чисел в диапазоне до {n}: {len(res)}')
    assert num < len(res)
    return res[num - 1]

test(1200)

finish = time.time()

print('Время выполнения алгоритма:', finish - start, 'сек')
print('-' * 60)

"""
Длина последовательности чисел: 2666667
На 304302 месте стоит простое число 1141127
Время выполнения алгоритма 1.6725361347198486 сек
"""

# Вариант 2. Используя алгоритм «Решето Эратосфена»

print('Используя алгоритм «Решето Эратосфена»')
n = 10000

start = time.time()

sieve = set(range(2, n + 1))
prost_list = []

while sieve:
    prime = min(sieve)
    prost_list.append(prime)
    sieve -= set(range(prime, n + 1, prime))

finish = time.time()

print(f'Длина последовательности чисел в диапазоне до {n}:', len(prost_list))
print('Время выполнения алгоритма:', finish - start, 'сек')

"""
Без использования «Решета Эратосфена»
Количество простых чисел в диапазоне до 10000: 1229
Время выполнения алгоритма: 0.013694524765014648 сек
------------------------------------------------------------
Используя алгоритм «Решето Эратосфена»
Длина последовательности чисел в диапазоне до 10000: 1229
Время выполнения алгоритма: 0.06633925437927246 сек
"""