f = open("text.txt", "r")
# x = f.read()  # чтение всего файла целиком
# x = f.read(10)  # чтение первых 10 символов(?)
# print(repr(x))  # ''''First\nSecond\nThird', repr - это однозначное (недвусмысленное) представление объекта
# в виде строки, такой, чтобы возможно было бы из этого представления сделать такой же объект'''
# x = x.splitlines()  # ['First', 'Second', 'Third']
# x = f.readline()  # считывание одной строки
# x = x.rstrip()  # убираем символы справа
# x = f.readline().rstrip()  # объединяем строки
for line in f:  # '''итерация по файлу object, эффективен по памяти. если после него запустить read(),
    # он вернет пустую строку так как все уже считано'''
    line = line.rstrip()
    print(repr(line))
x = f.read()

print(repr(x))

f.close()
