"""
Урок 7. Алгоритмы сортировки

1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""

import random


def bubble_sort(spisok):
    swapped = False
    for i in range(len(spisok) - 1, 0, -1):
        for j in range(i):
            if spisok[j] < spisok [j + 1]:
                spisok[j + 1], spisok [j] = spisok [j], spisok [j + 1]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return spisok


if __name__ == '__main__':
    print('\nСортировка целых чисел методом пузырька:')
    num_lst = []

    i = 10
    while i > 0:
        s = random.randint(-100, 100)
        num_lst.append(s)
        i -= 1

    print(num_lst, '- исходный список')
    print(bubble_sort(num_lst), '- отсортированный по убыванию список')

"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный 
и отсортированный массивы.
"""


def quick_sort(spisok):
    if len(spisok) < 2:
        return spisok
    pivot = spisok.pop()
    left_lst, equal_lst, right_lst = [], [pivot], []
    for i in spisok:
        if float(format(i, '.2f')) == float(format(pivot, '.2f')):
            equal_lst.append(i)
        elif i > pivot:
            right_lst.append(i)
        else:
            left_lst.append(i)
    return quick_sort(left_lst) + equal_lst + quick_sort(right_lst)


if __name__ == '__main__':
    print('\nСортировка вещественных чисел методом слияния:')
    num_lst = []

    i = 10
    while i > 0:
        s = random.uniform(0, 50)
        num_lst.append(float(format(s, '.2f')))
        i -= 1

    print(num_lst, '- исходный список')
    print(quick_sort(num_lst), '- отсортированный по возрастанию список')

"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две 
равные части: в одной находятся элементы, которые не меньше медианы, 
в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. 
Но если это слишком сложно, то используйте метод сортировки, 
который не рассматривался на уроках
"""


def mediana(num_lst):
    print(*num_lst, '- исходный список')
    print(*(sorted(num_lst)), '- отсортированный список')
    idx = len(num_lst) // 2
    if len(num_lst) % 2 != 0:
        return sorted(num_lst)[idx]
    return sum(sorted(num_lst)[idx - 1:idx + 1]) / 2


if __name__ == '__main__':
    n = int(input('Введите количество элементов в массиве: '))
    num_lst = []

    while n > 0:
        m = random.randint(0, 50)
        num_lst.append(2*m + 1)
        n -= 1

    print(mediana(num_lst), '- медиана списка')
