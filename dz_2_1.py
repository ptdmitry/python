my_tuple = 15 * 3, 15 / 3, 15 // 2, 15**2

for ind in range(len(my_tuple)):
      result = my_tuple[ind]
      class_result = type(my_tuple[ind])
      print(f'{result} - {class_result}')