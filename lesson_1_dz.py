"""
Урок 1. Введение в алгоритмизацию и реализация простых алгоритмов на Python

1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""


def sum_and_mult(num):
    if len(num) == 3:
        return(f'Сумма чисел: {int(num[0]) + int(num[1]) + int(num[2])}\n'
               f'Произведение чисел: {int(num[0]) * int(num[1]) * int(num[2])}')
    else:
        return(f'Ввели не трёхзначное число')


if __name__ == '__main__':
    print(sum_and_mult(str(input('Введите трёхзначное число: '))))

"""
2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
"""


def logical(x, y):
    return (
        f'И: {x} & {y} = {x & y}\n'
        f'ИЛИ: {x} | {y} = {x | y}\n'
        f'Исключающее ИЛИ: {x} ^ {y} = {x ^ y}\n'
        f'Сдвиг влево: {x} << 2 = {x << 2}\n'
        f'Сдвиг вправо: {x} >> 2 = {x >> 2}'
    )


if __name__ == '__main__':
    print(logical(5, 6))

"""
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
проходящей через эти точки.
"""


def equation(x_1, y_1, x_2, y_2):
    return(f'Уравнение прямой: y = ({(y_2 - y_1) / (x_2 - x_1)}) * x + '
           f'({y_1 - (x_1 * (y_2 - y_1)) / (x_2 - x_1)})')


if __name__ == '__main__':
     print(equation((int(input('Введите координаты точки "A". x1 = '))),
                    (int(input('Введите координаты точки "A": y1 = '))),
                    (int(input('Введите координаты точки "B". x2 = '))),
                    (int(input('Введите координаты точки "B": y2 = ')))))

"""
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. Например,
если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

import random


def random_choice(x, y, n):
    if int(n) == 1 and int(y) > int(x):
        return(f'Произвольное число из диапазона {x} - {y}: {random.randint(int(x), int(y))}')
    elif int(n) == 1 and int(y) < int(x):
        return (f'Произвольное число из диапазона {x} - {y}: {random.randint(int(y), int(x))}')
    elif int(n) == 2 and float(y) > float(x):
        return(f'Произвольное число из диапазона {x} - {y}: '
               f'{float("{:.2f}".format(random.uniform(float(x), float(y))))}')
    elif int(n) == 2 and float(y) < float(x):
        return(f'Произвольное число из диапазона {x} - {y}: '
               f'{float("{:.2f}".format(random.uniform(float(y), float(x))))}')
    elif int(n) == 3 and ord(y) > ord(x):
        return(f'Произвольный символ из диапазона {x} - {y}: {chr(random.randint(ord(x), ord(y)))}')
    elif int(n) == 3 and ord(y) < ord(x):
        return(f'Произвольный символ из диапазона {x} - {y}: {chr(random.randint(ord(y), ord(x)))}')
    else:
        return(f'Некорректно введены данные')


if __name__ == '__main__':
    print(random_choice((input('Введите начало диапазона выборки: ')),
                        (input('Введите конец диапазона выборки: ')),
                        (input('Указанный диапазон - это: 1 - целые числа, '
                                   '2 - вещественные числа, 3 - символы: '))))

"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

def letters(first_letter, second_letter):
    alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
    if alphabet_eng.index(second_letter) > alphabet_eng.index(first_letter):
        return (f'Место буквы {first_letter} - {alphabet_eng.index(first_letter) + 1}\n'
                f'Место буквы {second_letter} - {alphabet_eng.index(second_letter) + 1}\n'
                f'Количество букв между ними: '
                f'{alphabet_eng.index(second_letter) - alphabet_eng.index(first_letter) - 1}')
    elif alphabet_eng.index(second_letter) < alphabet_eng.index(first_letter):
        return (f'Место буквы {first_letter} - {alphabet_eng.index(first_letter) + 1}\n'
                f'Место буквы {second_letter} - {alphabet_eng.index(second_letter) + 1}\n'
                f'Количество букв между ними: '
                f'{alphabet_eng.index(first_letter) - alphabet_eng.index(second_letter) - 1}')
    else:
        return (f'Некорректно введены данные')


if __name__ == '__main__':
    print(letters(input('Введите любую букву английского алфавита: '),
                  input('Введите ещё одну любую букву английского алфавита: ')))

"""
6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""


def letter(user_num_letter):
    alphabet_eng = 'abcdefghijklmnopqrstuvwxyz'
    return (f'Буква под номером {user_num_letter} - это: "{alphabet_eng[user_num_letter - 1]}"')


if __name__ == '__main__':
    print(letter(int(input('Введите число от 1 до 26: '))))

"""
7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить,
является ли он разносторонним, равнобедренным или равносторонним.
"""


def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return (f'Таких треугольников не существует')
    elif a == b == c:
        return (f'Треугольник равносторонний')
    elif a == b != c or a == c != b or b == c != a:
        return (f'Треугольник равнобедренный')
    elif a != b != c:
        return (f'Треугольник разносторонний')


if __name__ == '__main__':
    print(triangle(int(input('Введите отрезок "а" треугольника: ')),
                   int(input('Введите отрезок "b" треугольника: ')),
                   int(input('Введите отрезок "c" треугольника: '))))

"""
8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""


def years(year):
    if year % 4 == 0:
        return (f'Год {year} високосный')
    else:
        return (f'Год {year} не високосный')


if __name__ == '__main__':
    print(years(int(input('Введите год (например - 2020: '))))

"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""


def numbers(a, b, c):
    if a > b:
        if b > c:
            return (f'Среднее число по величине - {b}')
        elif a > c:
            return (f'Среднее число по величине - {c}')
        else:
            return (f'Среднее число по величине - {a}')
    elif a < b:
        if b < c:
            return (f'Среднее число по величине - {b}')
        elif a < c:
            return (f'Среднее число по величине - {c}')
        else:
            return (f'Среднее число по величине - {a}')


if __name__ == '__main__':
    print(numbers(int(input('Введите 1-е число: ')),
                  int(input('Введите 2-е число: ')),
                  int(input('Введите 3-е число: '))))
