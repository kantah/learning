"Библиотека operator"
import operator as op

print(op.add(4, 5))  # 9, сложение
print(op.mul(4, 5))  # 20, умножение
print((op.contains([1, 2, 3], 4)))  # False, проверяем содержит ли список [1, 2, 3] четверку == 4 in [1, 2, 3]

x = [1, 2, 3]
f = op.itemgetter(1)  # f(x) == x[1], itemgetter имитирует квадратную скобку
print(f(x))  # 2

x = [("Guido", 'Van', "Rossum"), ("Haskell", "Curry"), ("John", "Backus")]
f = op.attrgetter("sort")  # f(x) == x.sort
print(f(x))  # <built-in method sort of list object at 0x0000024626850140>
print(x)  # [('Guido', 'Van', 'Rossum'), ('Haskell', 'Curry'), ('John', 'Backus')]

"Пример использования itemgetter. Сортируем имена по последнему элементу"
x = [("Guido", 'Van', "Rossum"), ("Haskell", "Curry"), ("John", "Backus")]
x.sort(key=op.itemgetter(-1))  # [('Guido', 'Van', 'Rossum'), ('Haskell', 'Curry'), ('John', 'Backus')]
print(x)
