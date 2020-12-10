import json

student1 = {
    "first_name": "Oleg",
    "last_name": "Dean",
    "certificate": True,
    "scores": [
        70,
        80,
        90
    ],
    "description": "Good job, Greg"
}
student2 = {
    "first_name": "Wirl",
    "last_name": "Wood",
    "certificate": True,
    "scores": [
        70,
        80,
        90
    ],
    "description": "Nicely Done"
}
data = [student1, student2]
print(json.dumps(data, indent=4, sort_keys=True))  # функция dumps принимает объект python в качестве первого аргумента
# и возвращает строковое представление в формате json.  indent - количество отступов, которые нужно использовать в
# списках и словарях. key_sort - отсортировать ключи каждого словаря, который попадается в данном объекте.
# [
#     {
#         "certificate": true,
#         "description": "Good job, Greg",
#         "first_name": "Oleg",
#         "last_name": "Dean",
#         "scores": [
#             70,
#             80,
#             90
#         ]
#     },
#     {
#         "certificate": true,
#         "description": "Nicely Done",
#         "first_name": "Wirl",
#         "last_name": "Wood",
#         "scores": [
#             70,
#             80,
#             90
#         ]
#     }
# ]

# Чтобы записать данные в файл, нужно использовать фуекцию dump вместо dumps и вторым аргументом передать файл object
with open("students.json", 'w') as f:
    json.dump(data, f, indent=4, sort_keys=True)

# Чтобы получить объект python, соответствующий строковому представлению в формате json, мы можем использовать функцию
# loads. loads принимает в качестве первого агрумента строку в формате json и возвращает соответствующий ей объект
# python
import json

student1 = {
    "first_name": "Oleg",
    "last_name": "Dean",
    "certificate": True,
    "scores": [
        70,
        80,
        90
    ],
    "description": "Good job, Greg"
}
student2 = {
    "first_name": "Wirl",
    "last_name": "Wood",
    "certificate": True,
    "scores": [
        70,
        80,
        90
    ],
    "description": "Nicely Done"
}
data = [student1, student2]  # объект python
data_json = json.dumps(data, indent=4, sort_keys=True)  # получаем строку json из объекта python
data_again = json.loads(data_json)  # получаем объект python из строки json
print(sum(data_again[0]['scores']))  # печатаем сумму значений ключа scores первого словаря
# 240

# чтобы считать данные из файла используем функцию load
with open("students.json") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"]))
# 240.2
