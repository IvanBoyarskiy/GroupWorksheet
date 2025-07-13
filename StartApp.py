import sys
import tkinter as tk
from tkinter import filedialog
import os
import win32com.client


# === Функция для создания ярлыка ===
def create_shortcut(target_path, shortcut_name, folder):
    desktop = folder
    path = os.path.join(desktop, f"{shortcut_name}.lnk")
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = os.path.dirname(target_path)
    shortcut.IconLocation = "python.exe"  # Можно заменить на .ico файл
    shortcut.save()


def get_project_dir():
    if getattr(sys, 'frozen', False):
        # Если запущено из .exe
        return os.path.dirname(sys.executable)
    else:
        # Если запущено как обычный .py файл
        return os.path.dirname(os.path.abspath(__file__))



# === Ваша функция save_path ===
def save_path(selected_folder):
    print(f"Выбранная папка: {selected_folder}")

    # Пути к вашим питон-файлам
    project_dir = get_project_dir()
    group_script = os.path.join(project_dir, "FileGroup.py")
    ungroup_script = os.path.join(project_dir, "FileUngroup.py")

    # === Новое: запись пути в файл worksheetpath.txt ===
    worksheet_file = os.path.join(project_dir, "worksheetpath.txt")

    try:
        with open(worksheet_file, 'w', encoding='utf-8') as f:
            f.write(selected_folder)  # Записываем выбранный путь
        print(f"Путь сохранён в {worksheet_file}")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

    # Создание ярлыков
    create_shortcut(group_script, "Группировать", selected_folder)
    create_shortcut(ungroup_script, "Разгруппировать", selected_folder)


# === GUI ===
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        save_path(folder_selected)
        root.destroy()  # Закрыть окно после выбора


# === Запуск GUI ===
root = tk.Tk()
root.title("Выбор папки")
root.geometry("400x150")

label = tk.Label(root, text="Выберите папку для установки ярлыков:", pady=20)
label.pack()

button = tk.Button(root, text="Выбрать папку", command=select_folder)
button.pack()

root.mainloop()