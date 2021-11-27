staff = ('Иван', 'Мария', 'Пётр', 'Илья', 'Михаил')
dict_staff = {}


def thesaurus(staff):
    for name in staff:
        dict_staff.setdefault(name[:1].title(), []).append(name)
    print(dict_staff)


thesaurus(staff)