cube_list = []
num_sum = 0
all_sum = 0
new_num_sum = 0
new_all_sum = 0

for i in range(1000):
    if i % 2 != 0:
        cube_list.append(i ** 3)

for num in cube_list:
    num_sum = num // 100000000 + num // 10000000 % 10 + \
              num // 1000000 % 10 + num // 100000 % 10 + \
              num // 10000 % 10 + num // 1000 % 10 + \
              num // 100 % 10 + num // 10 % 10 + num % 10
    if num_sum % 7 == 0:
        all_sum += num

print(all_sum)

for p, num in enumerate(cube_list):
    cube_list[p] += + 17

for num in cube_list:
    new_num_sum = num // 100000000 + num // 10000000 % 10 + \
              num // 1000000 % 10 + num // 100000 % 10 + \
              num // 10000 % 10 + num // 1000 % 10 + \
              num // 100 % 10 + num // 10 % 10 + num % 10
    if new_num_sum % 7 == 0:
       new_all_sum += num

print(new_all_sum)