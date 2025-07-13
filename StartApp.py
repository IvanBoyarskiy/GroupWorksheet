import sys
import os
import tkinter as tk
from tkinter import filedialog
import win32com.client


# === Получение пути к проекту ===
def get_project_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


# === Создание ярлыка на .exe файл ===
def create_shortcut(target_path, shortcut_name, folder):
    shortcut_path = os.path.join(folder, f"{shortcut_name}.lnk")

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target_path  # Теперь это .exe
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.IconLocation = target_path  # Иконка от .exe
    try:
        shortcut.save()
        print(f"Ярлык '{shortcut_name}' создан: {shortcut_path}")
    except Exception as e:
        print(f"Ошибка при создании ярлыка '{shortcut_name}': {e}")


# === Функция сохранения пути и создания ярлыков ===
def save_path(selected_folder):
    print(f"Выбранная папка: {selected_folder}")

    project_dir = get_project_dir()

    group_exe = os.path.join(project_dir, "dist/FileGroup.exe")
    ungroup_exe = os.path.join(project_dir, "dist/FileRegroup.exe")

    worksheet_file = os.path.join(project_dir, "worksheetpath.txt")
    try:
        with open(worksheet_file, 'w', encoding='utf-8') as f:
            f.write(selected_folder)
        print(f"Путь сохранён в {worksheet_file}")
    except Exception as e:
        print(f"Ошибка записи файла: {e}")

    create_shortcut(group_exe, "Группировать", selected_folder)
    create_shortcut(ungroup_exe, "Разгруппировать", selected_folder)
    root.destroy()


# === GUI ===
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        save_path(folder)


root = tk.Tk()
root.title("Выбор папки")
root.geometry("400x150")

tk.Label(root, text="Выберите папку для установки ярлыков:", pady=20).pack()
tk.Button(root, text="Выбрать папку", command=select_folder).pack()

root.mainloop()