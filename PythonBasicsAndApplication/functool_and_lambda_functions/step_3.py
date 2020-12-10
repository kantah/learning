"Задача: отсортировать имена по длине"
x = [("Guido", 'Van', "Rossum"), ("Haskell", "Curry"), ("John", "Backus")]
def length(name):
    return len("".join(name))  # разрезаем имена по пробелу, склеиваем и выводим длину
x.sort(key=length)  # сортируем по длине, используя функции key и length
print(x)

"Сокращаем код с помощью lambda"
x.sort(key=lambda name: len("".join(name)))
print(x)
