import os
import shutil
import sys
import tkinter as tk
from tkinter import filedialog

import pylnk3

APP_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

def create_shortcut_pylnk3(target, shortcut_name, desktop_path, icon=None, work_dir=None):
    try:
        shortcut_path = os.path.join(desktop_path, f"{shortcut_name}.lnk")
        print(f"Создаю ярлык: {shortcut_path}")

        lnk = pylnk3.for_file(target)
        if icon and os.path.exists(icon):
            lnk.icon_location = icon
        else:
            print("❌ Иконка не найдена или не указана")

        lnk.work_dir = work_dir or os.path.dirname(target)
        lnk.save(shortcut_path)

        print(f"✅ Ярлык успешно создан: {shortcut_path}")
        if shortcut_path and os.path.exists(shortcut_path):
            print("✅ Реально создано")
        else:
            print("❌ Реально не создано")
        os.chmod(shortcut_path, 0o777)
        with open(shortcut_path, 'rb') as f:
            content = f.read(100)
            print(f"Первые байты файла: {content}")
        return shortcut_path
    except Exception as e:
        print(f"❌ Ошибка при создании ярлыка: {e}")
        return None
def save_to_txt(filename, user_text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(user_text)
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
def resource_path(relative_path):
    return os.path.join(APP_DIR, relative_path)

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        path.config(text=folder_path)
        save_to_txt(resource_path('txts/worksheetpath.txt'), folder_path)
        print(path.cget("text"))
def save_to_files():


    if entry_app.get().strip() == "":
        save_to_txt(resource_path('txts/appfilesname.txt'), "AppFiles")
    else:
        save_to_txt(resource_path('txts/appfilesname.txt'), entry_app.get())
    if entry_arc.get().strip() == "":
        save_to_txt(resource_path('txts/archivefilesname.txt'), "ArchiveFiles")
    else:
        save_to_txt(resource_path('txts/archivefilesname.txt'), entry_arc.get())
    if entry_aud.get().strip() == "":
        save_to_txt(resource_path('txts/audiofilesname.txt'), "AudioFiles")
    else:
        save_to_txt(resource_path('txts/audiofilesname.txt'), entry_aud.get())
    if entry_code.get().strip() == "":
        save_to_txt(resource_path('txts/codefilesname.txt'), "CodeFiles")
    else:
        save_to_txt(resource_path('txts/codefilesname.txt'), entry_code.get())
    if entry_doc.get().strip() == "":
        save_to_txt(resource_path('txts/documentfilesname.txt'), "DocumentFiles")
    else:
        save_to_txt(resource_path('txts/documentfilesname.txt'), entry_doc.get())
    if entry_img.get().strip() == "":
        save_to_txt(resource_path('txts/imagefilesname.txt'), "ImageFiles")
    else:
        save_to_txt(resource_path('txts/imagefilesname.txt'), entry_img.get())
    if entry_shr.get().strip() == "":
        save_to_txt(resource_path('txts/shortcutfilesname.txt'), "ShortcutFiles")
    else:
        save_to_txt(resource_path('txts/shortcutfilesname.txt'), entry_shr.get())
    if entry_vid.get().strip() == "":
        save_to_txt(resource_path('txts/videofilesname.txt'), "VideoFiles")
    else:
        save_to_txt(resource_path('txts/videofilesname.txt'), entry_vid.get())

    create_shortcut_pylnk3(
        target=f"{resource_path("dist/FileGroup.exe")}",
        desktop_path=get_from_txt(resource_path('txts/worksheetpath.txt')),
        shortcut_name="Группировать",
        icon=f"{resource_path("assets/group.ico")}",
        work_dir=f"{resource_path("dist")}"
    )

    create_shortcut_pylnk3(
        target=f"{resource_path("dist/FileRegroup.exe")}",
        desktop_path=get_from_txt(resource_path('txts/worksheetpath.txt')),
        shortcut_name="Разгруппировать",
        icon=f"{resource_path("assets/regroup.ico")}",
        work_dir=f"{resource_path("dist")}"
    )

    window.destroy()


window = tk.Tk()
window.title("Настройки Группировщика")
window.geometry('600x450')

frame_main = tk.Frame(window)
frame_main.grid(row=0, column=0)

label_1 = tk.Label(frame_main, text="Выберете путь к Рабочему столу", font=("Arial", 14))
label_1.pack(side=tk.TOP, pady=10)
path = tk.Label(frame_main, text="Папка не выбрана", font=("Arial", 12))
path.pack(pady=5)
path.config(text=get_from_txt(resource_path('txts/worksheetpath.txt')))

button = tk.Button(frame_main, text="Выбрать папку", command=select_folder)
button.pack(pady=10)

frame = tk.Frame(window)
frame.grid(row=0, column=1, padx=50, pady=20)

label_2 = tk.Label(frame, text="Выберите названия", font=("Arial", 14))
label_2.pack()

label_app = tk.Label(frame, text="Приложения (.exe и т.п.):")
label_app.pack()
entry_app = tk.Entry(frame, width=20)
entry_app.pack(padx=5)
entry_app.insert(0, get_from_txt(resource_path('txts/appfilesname.txt')))

label_arc = tk.Label(frame, text="Архивы (.zip и т.п.):")
label_arc.pack()
entry_arc = tk.Entry(frame, width=20)
entry_arc.pack(padx=5)
entry_arc.insert(0, get_from_txt(resource_path('txts/archivefilesname.txt')))

label_aud = tk.Label(frame, text="Аудио (.mp3 и т.п.):")
label_aud.pack()
entry_aud = tk.Entry(frame, width=20)
entry_aud.pack(padx=5)
entry_aud.insert(0, get_from_txt(resource_path('txts/audiofilesname.txt')))

label_code = tk.Label(frame, text="Программирование (.py и т.п.):")
label_code.pack()
entry_code = tk.Entry(frame, width=20)
entry_code.pack(padx=5)
entry_code.insert(0, get_from_txt(resource_path('txts/codefilesname.txt')))

label_doc = tk.Label(frame, text="Документы (.txt и т.п.):")
label_doc.pack()
entry_doc = tk.Entry(frame, width=20)
entry_doc.pack(padx=5)
entry_doc.insert(0, get_from_txt(resource_path('txts/documentfilesname.txt')))

label_img = tk.Label(frame, text="Изображения (.jpg и т.п.):")
label_img.pack()
entry_img = tk.Entry(frame, width=20)
entry_img.pack(padx=5)
entry_img.insert(0, get_from_txt(resource_path('txts/imagefilesname.txt')))

label_shr = tk.Label(frame, text="Ярлыки (.lnk и т.п.):")
label_shr.pack()
entry_shr = tk.Entry(frame, width=20)
entry_shr.pack(padx=5)
entry_shr.insert(0, get_from_txt(resource_path('txts/shortcutfilesname.txt')))

label_vid = tk.Label(frame, text="Видео (.mp4 и т.п.):")
label_vid.pack()
entry_vid = tk.Entry(frame, width=20)
entry_vid.pack(padx=5, pady=5)
entry_vid.insert(0, get_from_txt(resource_path('txts/videofilesname.txt')))


close_button = tk.Button(window, text="Сохранить", command=save_to_files)
close_button.grid(row=1, column=0)


window.mainloop()