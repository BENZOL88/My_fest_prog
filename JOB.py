from tkinter import *
from tkinter import ttk
import os
import re
import json

name_dict = {}  # Словарь для хранения старого и нового имени файлов
data_file = "name_dict.json"  # Имя файла для хранения данных

def save_data():
    global name_dict, data_file
    with open(data_file, 'w') as f:
        json.dump(name_dict, f)

def load_data():
    global name_dict, data_file
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            name_dict = json.load(f)

def rename(event):
    global name_dict

    # Получение списка файлов в директории
    s = ent.get()
    e = ent1.get()
    directory = s  # Замените на фактический путь к директории
    files = os.listdir(directory)

    # Применение регулярного выражения для переименования файлов
    for filename in files:
        new_filename = re.sub(r'.*?' + e, '', filename)
        old_name = filename  # Запоминаем старое имя
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        name_dict[new_filename] = old_name  # Добавляем новое имя и его старое значение в словарь

def count(event):
    s = ent.get()
    folder_path = s
    output_file = s+'\\result.txt'

    file_names = os.listdir(folder_path)

    with open(output_file, 'w') as f:
        for name in file_names:
            f.write(name + '\n')

def restore_names(event):
    global name_dict

    # Получение списка файлов в директории
    s = ent.get()
    directory = s  # Замените на фактический путь к директории
    files = os.listdir(directory)

    # Восстановление старых имен файлов
    for filename in files:
        if filename in name_dict:
            old_name = name_dict[filename]
            os.rename(os.path.join(directory, filename), os.path.join(directory, old_name))

root = Tk()
root.title('My prog')

La1 = Label(text='Введите символ до которого стираем название')
ent1 = Entry(width=60)
La = Label(text='Введите путь к папке')
ent = Entry(width=60)
but = Button(text="Преобразовать")
but2 = Button(text="Пересчет")
but3 = Button(text="Восстановить имена")

but.bind('<Button-1>', rename)
but2.bind('<Button-1>', count)
but3.bind('<Button-1>', restore_names)

La1.pack()
ent1.pack()
La.pack()
ent.pack()
but.pack()
but2.pack()
but3.pack()

# Загружаем данные при запуске программы
load_data()

root.mainloop()
