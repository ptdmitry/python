with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()
for i in content:
    f_cont = (f"({i.split(' ')[0]}, {i.split(' ')[5][1:]}, {i.split(' ')[6]})\n")
    print(f_cont, end='')
    with open('content_github.txt', 'a', encoding='utf-8') as f:
        f.write(f_cont)
