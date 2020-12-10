# Форматирование format позволяет выполнить подстановку значения в шаблон
capital = "London is the capital of Great Britain"
template = "{} is the capital of {}"
print(template.format("London", "Great Britain"))  # London is the capital of Great Britain
print(template.format("Vaduz", "Liechtenstein"))  # Vadus is the capital of Liechtenstein
# Внутри фигурных скобок можно указать порядок, в котором принимаются аргументы
template = "{1} is the capital of {0}"
print(template.format("London", "Great Britain"))  # Great Britain is the capital of London
print(template.format("Vaduz", "Liechtenstein"))  # Liechtenstein is the capital of Vadus
# Можно использовать именованные аргументы. Тогда порядок аргументов может быть любым
template = "{capital} is the capital of {country}"
print(template.format(capital="London", country="Great Britain"))
print(template.format(capital="Vaduz", country="Liechtenstein"))

# Благодаря форматированию, мы можем обращаться к аттрибутам объектов, которые мы передали
import requests
template = "Response from {0.url} with code {0.status_code}"
res = requests.get("https://doc.python.org/3.5/")
print(template.format(res))  # Response from https://docs.python.org/3.5/ with code 200
res = requests.get("https://doc.python.org/3.5/random")
print(template.format(res))  # Response from https://docs.python.org/3.5/random with code 404

# С помощью format можно указать сколько знаков после запятой нас интересуют
from random import random
x = random()
print(x)  # 0.17175737257869994
print("{:.3}".format(x))  # 0.172
