# Метод lower возвращает копию строки, в которой все буквы находятся в нижнем регистре. Небуквенные символы не
# изменяются
s = "The man in black fled across the desert"
print(s.lower())  # the man in black fled across the desert

# Метод upper возвращает копию строки, в которой все символы находятся в верхнем регистре
s = "The man in black fled across the desert"
print(s.upper())  # THE MAN IN BLACK FLED ACROSS THE DESERT

# Метод replace позволяет найти все вхождения строки, переданной первым аргументом, и заменить ее строкой,
# переданной вторым аргументом.
s = "The man in black fled across the desert"
print(s.replace("a", "@"))  # The m@n in bl@ck fled @cross the desert
#  Третьим аргументом можно передать число, сколько раз нужно выполнить замену
s = "The man in black fled across the desert"
print(s.replace("a", "@", 2))  # The m@n in bl@ck fled across the desert

# Метод split позволяет разделить строку по заданному символу. По умолчанию удаляются все пробельные символы
# и пустые строки
print(s.split())  # ['The', 'man', 'in', 'black', 'fled', 'across', 'the', 'desert']
# Принимает аргумент maxsplit, показывающий сколько изменений мы можем сделать
print((s.split(" ", 3)))  # ['The', 'man', 'in', 'black fled across the desert']

# Методы strip удаляют указанные символы слева и справа строки. По умолчанию удаляются пробелы
print(s.lower().strip("t"))  # he man in black fled across the deser
print(s.lower().lstrip("t"))  # he man in black fled across the desert
print(s.lower().rstrip("t"))  # the man in black fled across the deser

# Метод join принимает аргумент-последовательность и вставляет строку, от которой его вызвали между всеми элементами
# последовательности. Элементы последовательности всегда должны быть строками
print("@".join(['The', 'man', 'in', 'black', 'fled', 'across', 'the', 'desert']))
# The@man@in@black@fled@across@the@desert
