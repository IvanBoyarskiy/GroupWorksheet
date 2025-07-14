import shutil
import sys
from pathlib import Path
import os

APP_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

def resource_path(relative_path):
    return os.path.join(APP_DIR, relative_path)

def if_directory_exist(directory_path):
    if os.path.exists(directory_path):
        return True
    else:
        return False
def get_from_txt(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            path = file.readline().strip()
            if path:
                return path
            else:
                print("Файл существует, но он пуст.")
                return None
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return None
def send_files(files):
    for file in files:
        file_path = file[0]
        directory = file[1]
        directory.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file_path), str(directory))
def get_files(directory):
    dict = []
    for file_path in Path(f'{get_from_txt(resource_path("txts/worksheetpath.txt"))}\\{directory}').iterdir():
            get_info_file(file_path)
            full_path = file_path.resolve()
            dict.append([full_path, Path(get_from_txt(resource_path('txts/worksheetpath.txt')))])

    return dict
def get_info_file(file_path):
    print(f"Полный путь: {file_path.resolve()}")
    print(f"Папка: {file_path.parent}")
    print(f"Имя файла с расширением: {file_path.name}")
    print('-' * 40)
def ungroup(mas):
    for theme in mas:
        if if_directory_exist(f'{get_from_txt(resource_path('txts/worksheetpath.txt'))}\\{theme}'):
            files = get_files(theme)
            send_files(files)
        try:
            os.chmod(f'{get_from_txt(resource_path('txts/worksheetpath.txt'))}\\{theme}', 0o777)
            shutil.rmtree(f'{get_from_txt(resource_path('txts/worksheetpath.txt'))}\\{theme}')
        except:
            pass


themes = [get_from_txt(resource_path('txts/appfilesname.txt')), get_from_txt(resource_path('txts/archivefilesname.txt')),
          get_from_txt(resource_path('txts/audiofilesname.txt')), get_from_txt(resource_path('txts/codefilesname.txt')),
          get_from_txt(resource_path('txts/documentfilesname.txt')), get_from_txt(resource_path(
        'txts/imagefilesname.txt')),
          get_from_txt(resource_path('txts/shortcutfilesname.txt')), get_from_txt(resource_path(
        'txts/videofilesname.txt'))]
ungroup(themes)
