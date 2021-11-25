some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(f'{some_list[0].title()} "0{some_list[1]}" {some_list[2]} "{some_list[3]}" '
      f'{some_list[4]} {some_list[5]} {some_list[6]} {some_list[7]} '
      f'"+0{some_list[8].replace("+", "")}" {some_list[9]}')