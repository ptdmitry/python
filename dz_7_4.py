import os
import collections


def dir_info():
    root_dir = r'C:\Users\Admin\PycharmProjects\helloworld\venv\Lib\site-packages\aiohttp'
    aionhttp_files = collections.defaultdict(int)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = 10 ** len(str(os.stat(os.path.join(root, file)).st_size))
            aionhttp_files[size] += 1

    for size, nums in sorted(aionhttp_files.items()):
        print(f'{size}: {nums}')


dir_info()