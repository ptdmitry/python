"""
Урок 6. Работа с динамической памятью

1. Подсчитать, сколько было выделено памяти под переменные
в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее
эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы
или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
"""

import sys

"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй
массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
начинается с нуля), т.к. именно в этих позициях первого массива стоят
четные числа.
"""

my_list = [45, 5, 3, 8, 4, 6, 43, 44, 8, 22, 27, 30, 1, 2, 6, 10] # 56 + 8*16 = 184 байт
index_list = [] # 56 байт
print(f"Исходный список: {sys.getsizeof(my_list)} байт") # 184 байт
print(f"Итоговый список (пустой): {sys.getsizeof(index_list)} байт") # 56 байт

for i, value in enumerate(my_list):
    if value % 2 == 0:
        index_list.append(i)
    print(sys.getsizeof(index_list), end=' ') # 56 56 56 88 88 88 88 88 120 120 120 120 120 120 184 184
        # print(sys.getsizeof(i)) # 28 байт

print()
print(f"Итоговый список (заполненный): {index_list}")
print(f"Итоговый список (заполненный): {sys.getsizeof(index_list)} байт") # 184 байт
print(f"Итоговый список (заполненный) должен быть: {56 + 8 * len(index_list)}") # 136 байт

"""
Программа занимает 1048 байта (my_list = 632 байта и index_list = 416 байт)

В начале:
my_list = (56 + 8*16) + 28*16 = 632 байта (пустой список + 16 ссылок по 8 байт + 16 чисел по 28 байт)
index_list = 56 байт (пустой список)

В теле цикла for:
i = 28 байт (присваиваемое число из списка my_list для проверки)

Не понимаю почему при добавлении первого значения в список index_list, он становится равен резко 88 байт?
И так далее с последующими добавлениями. И также непонятно, почему итоговый список index_list равен 184 байт, как
исходный my_list, хотя значений на 6 элементов меньше?

По логике итоговый index_list = (56 + 8*10) + 28*10 = 416 байт

Версия Python 3.10.1
ОС Windows, 64-разрядная, процессор x64
"""
# --------------------------------------------------------------------------------------------------------------------
"""
6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше
введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, то вывести загаданное число.
"""

import random

random_num = random.randint(0, 100) # 28 байт
game_start = input('Угадайте число от 0 до 100 за 10 попыток. Нажмите "s" для начала игры: ') # 50 байт
try:
    if game_start == 's':
        i = 1 # 28 байт
        answer = int(input('Угадайте число от 0 до 100: ')) # 28 байт
        while i < 10:
            if answer > random_num:
                answer = int(input(f'Попробуйте ещё раз. Загаданное число меньше {answer}: ')) # 28 байт
            elif answer < random_num:
                answer = int(input(f'Попробуйте ещё раз. Загаданное число больше {answer}: ')) # 28 байт
            else:
                print(f'Вы угадали!')
                break
            i += 1 # 28 байт
        print(f'Правильный ответ {random_num}')
    else:
          print('Пока')
except ValueError:
    print('Ошибка. Вы ыыели не цифру')

"""
Программа занимает 106 байт

Из них - это хранение загаданного числа random_num = 28 байт,
переменная game_start = 50 байт (символ), переменная i = 28 байт

Версия Python 3.10.1
ОС Windows, 64-разрядная, процессор x64
"""

# --------------------------------------------------------------------------------------------------------------------
"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def numbers_even_uneven(num): # 50 байт
    num_even = '' # 49 байт
    num_uneven = '' # 49 байт
    for i in num:
        if int(i) % 2 == 0:
            num_even += i
        else:
            num_uneven += i
    return (f'Количество чётных цифр в числе {num}: {len(num_even)}, {sys.getsizeof(num_even)} байт\n'
            f'Количество нечётных цифр в числе {num}: {len(num_uneven)}, {sys.getsizeof(num_uneven)} байт')


if __name__ == '__main__':
    print(numbers_even_uneven(str(input(f'Введите любое число: '))))

"""
Программа занимает минимально 149 байт. При вводе числа в 1 000 000 000 000 занимает незначительно больше: 173 байта

Переменная num зависит от разрядности вписываемого числа: от 0 до 9 - 50 байт, от 10 до 99 - 51 байт и т.д.
по 1 байту при увеличении разряда. Тип переменной - строка
Переменные num_even и num_uneven весят по 49 байт каждая (строки)

Версия Python 3.10.1
ОС Windows, 64-разрядная, процессор x64
"""
