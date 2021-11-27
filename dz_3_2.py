nums = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
        'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
        'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

num = input('Enter a number: ')


def num_translate_adv(num):
    if num[0].isupper():
        print(nums.get(num.lower()).title())
    else:
        print(nums.get(num))


num_translate_adv(num)