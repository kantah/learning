x = [-1, -2, 0, 1, 2]
y = [i * i for i in x]  # [1, 4, 0, 1, 4]
"аналогично записи"
y = []
for i in x:
    y.append(i * i)

"Добавляем условный оператор if"
y = [i * i for i in x if i > 0]  # [1, 4]

"Вложенные циклы"
my_list = [(x, y) for x in range(3) for y in range(3) if y >= x]  # [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
"аналогично записи"
my_list = []
for x in range(3):
    for y in range(3):
        if y >= x:
            my_list.append((x, y))

"Множество"
my_set = {c for c in 'python'}  # {'n', 'o', 'p', 't', 'y', 'h'}

"Словарь"
my_dict = {i: ord(i) for i in 'python'}  # {'p': 112, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}
"Если список содержит последовательно пары key, value, его можно преобразовать в словарь"
my_list = ['name', 'Eric', 'second name', 'Cartman', 'age', 8]
my_dict = {my_list[i]: my_list[i + 1] for i in range(0, len(my_list), 2)}  # {'name': 'Eric', 'second name': 'Cartman',
# 'age': 8}
