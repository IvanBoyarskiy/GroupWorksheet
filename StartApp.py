import os
import tkinter as tk

def save_name(filename, user_text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(user_text)
def save_to_files():

    desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
    save_name('worksheetpath.txt', desktop)

    if entry_app.get().strip() == "":
            save_name('appfilesname.txt', "AppFiles")
    else:
            save_name('appfilesname.txt', entry_app.get())

    if entry_arc.get().strip() == "":
            save_name('archivefilesname.txt', "ArchiveFiles")
    else:
            save_name('archivefilesname.txt', entry_arc.get())

    if entry_aud.get().strip() == "":
            save_name('audiofilesname.txt', "AudioFiles")
    else:
            save_name('audiofilesname.txt', entry_aud.get())

    if entry_code.get().strip() == "":
            save_name('codefilesname.txt', "CodeFiles")
    else:
            save_name('codefilesname.txt', entry_code.get())

    if entry_doc.get().strip() == "":
            save_name('documentfilesname.txt', "DocumentFiles")
    else:
            save_name('documentfilesname.txt', entry_doc.get())

    if entry_img.get().strip() == "":
            save_name('imagefilesname.txt', "ImageFiles")
    else:
            save_name('imagefilesname.txt', entry_img.get())

    if entry_shr.get().strip() == "":
            save_name('shortcutfilesname.txt', "ShortcutFiles")
    else:
            save_name('shortcutfilesname.txt', entry_shr.get())

    if entry_vid.get().strip() == "":
            save_name('videofilesname.txt', "VideoFiles")
    else:
            save_name('videofilesname.txt', entry_vid.get())
    window.destroy()
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



window = tk.Tk()
window.title("Настройки Группировщика")
window.geometry('300x500')

frame = tk.Frame(window)
frame.pack()

label_2 = tk.Label(frame, text="Выберите названия", font=("Arial", 14))
label_2.pack(pady=20)

label_app = tk.Label(frame, text="Приложения (.exe и т.п.):")
label_app.pack()
entry_app = tk.Entry(frame, width=20)
entry_app.pack(padx=5)
entry_app.insert(0, get_from_txt('appfilesname.txt'))

label_arc = tk.Label(frame, text="Архивы (.zip и т.п.):")
label_arc.pack()
entry_arc = tk.Entry(frame, width=20)
entry_arc.pack(padx=5)
entry_arc.insert(0, get_from_txt('archivefilesname.txt'))

label_aud = tk.Label(frame, text="Аудио (.mp3 и т.п.):")
label_aud.pack()
entry_aud = tk.Entry(frame, width=20)
entry_aud.pack(padx=5)
entry_aud.insert(0, get_from_txt('audiofilesname.txt'))

label_code = tk.Label(frame, text="Программирование (.py и т.п.):")
label_code.pack()
entry_code = tk.Entry(frame, width=20)
entry_code.pack(padx=5)
entry_code.insert(0, get_from_txt('codefilesname.txt'))

label_doc = tk.Label(frame, text="Документы (.txt и т.п.):")
label_doc.pack()
entry_doc = tk.Entry(frame, width=20)
entry_doc.pack(padx=5)
entry_doc.insert(0, get_from_txt('documentfilesname.txt'))

label_img = tk.Label(frame, text="Изображения (.jpg и т.п.):")
label_img.pack()
entry_img = tk.Entry(frame, width=20)
entry_img.pack(padx=5)
entry_img.insert(0, get_from_txt('imagefilesname.txt'))

label_shr = tk.Label(frame, text="Ярлыки (.lnk и т.п.):")
label_shr.pack()
entry_shr = tk.Entry(frame, width=20)
entry_shr.pack(padx=5)
entry_shr.insert(0, get_from_txt('shortcutfilesname.txt'))

label_vid = tk.Label(frame, text="Видео (.mp4 и т.п.):")
label_vid.pack()
entry_vid = tk.Entry(frame, width=20)
entry_vid.pack(padx=5, pady=5)
entry_vid.insert(0, get_from_txt('videofilesname.txt'))


close_button = tk.Button(window, text="Сохранить", command=save_to_files)
close_button.pack(pady=20)


window.mainloop()