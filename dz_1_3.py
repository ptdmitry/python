procent = []

for i in range(101):
    procent.append(i)

for num in procent:
    if num % 10 == 1 and num != 11:
        print(procent[num], 'процент')
    elif 1 < num < 5 or 21 < num < 25 or \
            31 < num < 35 or 41 < num < 45 or \
            51 < num < 55 or 61 < num < 65 or \
            71 < num < 75 or 81 < num < 85 or \
            91 < num < 95:
        print(procent[num], 'процента')
    else:
        print(procent[num], 'процентов')
        num += num


