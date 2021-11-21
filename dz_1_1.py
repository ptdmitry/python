duration = int(input('Enter seconds: '))

if 0 < duration < 60 or \
    60 <= duration < 3600 or \
    3600 <= duration < 86400 or \
    86400 <= duration < 2678400:
    seconds = duration % 60
    minuts = duration // 60 % 60
    hours = duration // 3600 % 24
    days = duration // 86400
    print(days, 'дн', hours, 'час', minuts, 'мин', seconds, 'сек')
elif duration < 0:
    print('Enter positive number')
else:
    print('Too much seconds')

# Со списком:

duration = int(input('Enter seconds: '))

time_duration = [0, 'дн', 0, 'час', 0, 'мин', 0, 'сек']

if 0 < duration < 60 or \
        60 <= duration < 3600 or \
        3600 <= duration < 86400 or \
        86400 <= duration < 2678400:
    print('Enter positive number')
    seconds = duration % 60
    minuts = duration // 60 % 60
    hours = duration // 3600 % 24
    days = duration // 86400
    time_duration[-2] = seconds
    time_duration[4] = minuts
    time_duration[2] = hours
    time_duration[0] = days
    print(time_duration)
elif duration < 0:
    print('Enter positive number')
else:
    print('Too much seconds')