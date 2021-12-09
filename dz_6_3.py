from itertools import zip_longest

with open('users.csv', 'r', encoding='utf-8-sig') as f:
    user = f.readlines()
with open('hobby.csv', 'r', encoding='utf-8-sig') as f:
    hobby = f.readlines()

user = [line.rstrip() for line in user]
hobby = [line.rstrip() for line in hobby]
if len(user) >= len(hobby):
    dict_user_hobby = dict(zip_longest(user, hobby, fillvalue=None))
    with open('user_hobby.txt', 'w', encoding='utf-8-sig') as f:
        for key, val in dict_user_hobby.items():
            f.write(f"{key}: {val}\n")
else:
    exit(1)
