import requests


def is_interesting(num):
    num_url = "http://numbersapi.com/" + num + "/math?json=true"
    num_get = requests.get(num_url)
    num_data = num_get.json()
    return 'Interesting' if num_data['found'] else 'Boring'


with open('dataset_24476_3.txt') as numbers:
    for number in numbers:
        number = number.rstrip()
        print(is_interesting(number))
