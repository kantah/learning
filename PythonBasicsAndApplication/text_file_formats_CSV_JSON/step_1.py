import csv

with open("example.csv") as f:
    reader = csv.reader(f)
    for row in f:
        print(row)

# Если в файле у значения дробная часть отделена от целой не точкой а запятой, мы можем выделить значение кавычками
# student,good,90,"90,2",100

# Также если элемент записан в две строки, мы можем выделить его кавычками

# Можно явно указать символ в качестве разделителя. Пример: разделитель - табуляция. Указываем формат файла tsv и задаем
# для ридера дополнительный параметр: delimiter="\t"
with open("example.tsv") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in f:
        print(row)

# Чтобы записать файл в csv формате используется writer
students = [["student", "best", 100, 100, 100, "Excellent score"],
            ["student", "good", 90, 90.2, 100, "Good score, but could do better"]]
with open("example.csv", "a") as f:  # параметр "а" указывает, мы дописываем в конец файла
    writer = csv.writer(f)
    for student in students:
        writer.writerow(student)

# Вместо цикла for мы можем использовать метод writerows, который позволяет передавать список списков
with open("example.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerows(students)

# Мы можем уточнять некоторое поведение, которое нам требуется при записи. Например, нам необходимо поместить все
# элементы в кавычки. Для этого передаем специальный аргумент quoting
with open("example.csv", "a") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(students)
# используя константу QUOTE_ALL, мы заключаем в кавычки все элементы
