"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""
import csv
import re

with open('Crimes.csv') as crimes:
    reader = csv.reader(crimes)
    pattern = r".*\d\d/\d\d/2015"
    crimes_2016 = {}
    for row in crimes:
        row = row.rstrip()
        if re.search(pattern, row):
            row = row.split(',')
            if row[5] in crimes_2016:
                crimes_2016[row[5]] += 1
            else:
                crimes_2016[row[5]] = 1

print(crimes_2016)
print(max(crimes_2016, key=crimes_2016.get))
