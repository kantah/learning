
# f = open('test.txt', 'w')  # используем ключи 'w', 'r' и 'a'. Если такого файла не было, он будет создан
# f.write('Hello')
# f.write('world')  # Helloworld

# f.write('Hello\n')
# f.write('world')
# # Hello
# # world

# lines = ['Line_1', 'Line_2', 'Line_3']
# contens = '\n'.join(lines)
# f.write(contens)
# f.close()

"""Для записи в конец файла используется метод append(ключ "a")"""
f = open('test.txt', 'a')
f.write('Hello\n')

f.close()


