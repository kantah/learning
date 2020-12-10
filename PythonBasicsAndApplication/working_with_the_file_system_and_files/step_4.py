import os
import os.path
import shutil

print(os.listdir())  # показывает папки и файлы в директории, аргументы - путь

print(os.getcwd())  # показывает текущую директорию

print(os.path.exists())  # проверка существует ли файл или папка

print(os.path.isfile())  # проверяет, является ли путь файлом

print(os.path.isdir())  # проверяет, является ли путь папкой

print(os.path.abspath())  # выводит абсолютный путь

os.chdir()  # позволяет сменить текущую директорию

x = os.walk('.')  # позволяет пройтись по всем папкам и подпапкам в директории. аргумент "." - текущая директория
print(next(x))  # пошаговый обход
for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)

shutil.copy()  # копирует файлы или папки. первый аргумент - что копируем, второй - куда. библиотека shutil
