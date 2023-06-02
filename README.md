from tkinter import *
import os
import re

def rename(event):

	# Получение списка файлов в директории
	s = ent.get()
	directory = s  # Замените на фактический путь к директории
	files=os.listdir(directory)

	# Применение регулярного выражения для переименования файлов
	for filename in files:
		new_filename = re.sub(r'.*?@', '', filename)
		os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


root = Tk()
 
ent = Entry(width=60)
but = Button(text="Преобразовать")
lab = Label(width=20, bg='black', fg='white')
 
but.bind('<Button-1>', rename)


ent.pack()
but.pack()
root.mainloop()
