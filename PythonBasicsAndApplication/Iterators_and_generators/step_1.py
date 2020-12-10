"""Использование цикла for с print и end=' '"""
my_list = [1, 2, 3, 4, 5, 6]  # 1 2 3 4 5 6 - for перебирает элементы списка
my_dict = {'title': 'The Langoliers', 'author': 'Stephen King', 'year_published': 1990}  # title author year_published -
# ключи словаря
my_string = 'Hello, world'  # H e l l o ,   w o r l d - символы строки

for c in my_dict:
    print(c, end=' ')
"аналогично"
iterator = iter(my_dict)
print(next(iterator))  # title
print(next(iterator))  # author
print(next(iterator))  # year_published
print(next(iterator))  # StopIteration
"аналогично"
iterator = iter(my_dict)
while True:
    try:
        it = next((iterator))
        print(it)
    except StopIteration:
        break
