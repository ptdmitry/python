n = int(input('Enter a number: '))
nums_gen = (num for num in range(1, n + 1, 2))

print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))
print(*nums_gen)