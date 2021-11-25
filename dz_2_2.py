some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
second_some_list = []

for ind in some_list:
    if ind.isalpha():
        second_some_list.append(ind)
    elif int(ind) // 10 != 0:
        num = f'"{ind}"'
        second_some_list.append(num)
    elif ind[1:].isdigit():
        num = ind.replace('+', '')
        num = f'"+0{num}"'
        second_some_list.append(num)
    elif int(ind) // 10 == 0:
        num = f'"0{ind}"'
        second_some_list.append(num)

print(second_some_list)
print(' '.join(second_some_list))