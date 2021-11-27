nums = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
        'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
        'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

num = input('Enter a number: ')


def num_translate(num):
    print(nums.get(num))


num_translate(num)