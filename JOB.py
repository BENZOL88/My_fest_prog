from tkinter import *
from tkinter import ttk
import os
import re

def rename(event):

    # Получение списка файлов в директории
    s = ent.get()
    e = ent1.get()
    directory = s  # Замените на фактический путь к директории
    files=os.listdir(directory)

    # Применение регулярного выражения для переименования файлов
    for filename in files:
        new_filename = re.sub(r'.*?'+ e, '', filename)
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

def count(event):
    s = ent.get()
    folder_path = s
    output_file = s+'\\result.txt'

    file_names = os.listdir(folder_path)

    with open(output_file, 'w') as f:
        for name in file_names:
            f.write(name + '\n')


root = Tk()
root.title('My prog')

La1= Label(text='Введите символ до которого стираем название')
ent1 = Entry(width=60)
La= Label(text='Введите путь к папке')
ent = Entry(width=60)
but = Button(text="Преобразовать")
but2 = Button(text="Пересчет")
lab = Label(width=20, bg='black', fg='white')
 

but.bind('<Button-1>', rename)
but2.bind('<Button-1>', count)


La1.pack()
ent1.pack()
La.pack()
ent.pack()
but.pack()
but2.pack()
root.mainloop()