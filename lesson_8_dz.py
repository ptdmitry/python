"""
Урок 8. Деревья. Хэш-функция

1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

s = 'helloworld'

hash_set = set()

for i in range(len(s) + 1):
    for j in range(i + 1, len(s) + 1):
        h = hashlib.sha256(s[i:j].encode('utf-8')).hexdigest()
        hash_set.add(h)

print(f'Количество различных подстрок в строке "{s}": {len(hash_set)}')

"""
2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(head, codes={}, code=''):
    if head is None:
        return None
    if isinstance(head.value, str):
        codes[head.value] = code
        return codes
    get_code(head.left, codes, code+'0')
    get_code(head.right, codes, code+'1')
    return codes


def get_tree(temp):
    count_str = Counter(temp)
    if len(count_str) <= 1:
        node = Node(None)
        if len(count_str) == 1:
            node.left = Node(count_str[0])
            node.right = Node
        count_str = {node: 1}
    while len(count_str) != 1:
        node = Node(None)
        spam = count_str.most_common()[:-3:-1]
        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])
        else:
            node.left = spam[0][0]
        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])
        else:
            node.right = spam[1][0]
        del count_str[spam[0][0]]
        del count_str[spam[1][0]]
        count_str[node] = spam[0][1] + spam[1][1]
    return [key for key in count_str][0]


def coding(string, codes):
    res = ''
    for symbol in string:
        res += codes[symbol]
    return res


def decoding(string, codes):
    res = ''
    i = 0
    while i < len(string):
        for code in codes:
            if string[i:].find(codes[code]) == 0:
                res += code
                i += len(codes[code])
    return res


count_str = input('Введите строку для сжатия: ')
tree = get_tree(count_str)

codes = get_code(tree)
print(f'Шифр: {codes}')

coding_str = coding(count_str, codes)
print('Сжатая строка: ', coding_str)

decoding_str = decoding(coding_str, codes)
print('Исходная строка: ', decoding_str)
