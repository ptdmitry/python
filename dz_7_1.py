import os

dir_names = "my_project, settings, mainapp, adminapp, authapp"

try:
    if not os.path.exists(dir_names):
        os.mkdir(dir_names.split(',')[0])
except FileExistsError as e:
    print(f'Такая директория уже существует: {e.filename}')
os.chdir(dir_names.split(',')[0])
try:
    if not os.path.exists(dir_names):
        for i in dir_names.split(',')[1:]:
            all_dirs = os.mkdir(i)
except FileExistsError as e:
    print(f'Такая директория уже существует: {e.filename}')



# dir_names = "my_project, settings, mainapp, adminapp, authapp"
#
# try:
#     if not os.path.exists(dir_names):
#         os.mkdir(dir_names.split(',')[0])
# except FileExistsError as e:
#     print(f'Такая директория уже существует: {e.filename}', exit(1))
#     os.chdir(dir_names.split(',')[0])
#     if not os.path.exists(dir_names):
#         for i in dir_names.split(',')[1:]:
#             all_dirs = os.mkdir(i)