from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Пётр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Василий',
    'Инокентий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tutor_klass = (f"({name}, {klass})" for name, klass in zip_longest(tutors, klasses, fillvalue=None))

print(tutor_klass)
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))
print(next(tutor_klass))