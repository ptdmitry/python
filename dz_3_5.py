nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом', 'шкаф']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['весёлый', 'яркий', 'зелёный', 'утопичный', 'мягкий']
jokes = []

from random import choice


def get_jokes(num):
    i = 0
    while i < num:
        joke = f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}'
        jokes.append(joke)
        i += 1
    print(jokes)


get_jokes(2)