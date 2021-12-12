import os
import shutil

root_dir = r'C:\Users\Admin\PycharmProjects\helloworld\dz\my_project'
try:
    if os.path.exists(r'my_project\templates'):
        os.mkdir(r'my_project\templates')
except FileExistsError as e:
    print(f'Такая директория уже существует: {e.filename}')

src_1 = r'C:\Users\Admin\PycharmProjects\helloworld\dz\my_project\authapp\templates'
src_2 = r'C:\Users\Admin\PycharmProjects\helloworld\dz\my_project\mainapp\templates'
dst = r'C:\Users\Admin\PycharmProjects\helloworld\dz\my_project\templates'
try:
    for item in os.listdir(src_1):
        s_1 = os.path.join(src_1, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s_1):
            shutil.copytree(s_1, d)
        else:
            shutil.copy2(s_1, d)
except FileExistsError as e:
    print(f'Такая директория уже существует: {e.filename}')
try:
    for item in os.listdir(src_2):
        s_2 = os.path.join(src_2, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s_2):
            shutil.copytree(s_2, d)
        else:
            shutil.copy2(s_2, d)
except FileExistsError as e:
    print(f'Такая директория уже существует: {e.filename}')
    exit(1)

# root_dir = r'C:\Users\Admin\PycharmProjects\helloworld\dz\my_project'
# if not os.path.exists(r'my_project\templates'):
#     os.mkdir(r'my_project\templates')
#
# src_1 = r'C:\Users\Admin\PycharmProjects\helloworld\dz\my_project\authapp\templates'
# src_2 = r'C:\Users\Admin\PycharmProjects\helloworld\dz\my_project\mainapp\templates'
# dst = r'C:\Users\Admin\PycharmProjects\helloworld\dz\my_project\templates'
#
# for item in os.listdir(src_1):
#     s_1 = os.path.join(src_1, item)
#     d = os.path.join(dst, item)
#     if os.path.isdir(s_1):
#         shutil.copytree(s_1, d)
#     else:
#         shutil.copy2(s_1, d)
# for item in os.listdir(src_2):
#     s_2 = os.path.join(src_2, item)
#     d = os.path.join(dst, item)
#     if os.path.isdir(s_2):
#         shutil.copytree(s_2, d)
#     else:
#         shutil.copy2(s_2, d)