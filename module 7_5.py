import os, time

directory = os.walk('.')
for root, dirs, files in os.walk(r'C:\Users\541\Documents\Надя\Курс Python - разработчик\Модуль 7 Файлы'):
    for file in files:
        filepath = os.path.join(root,file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
