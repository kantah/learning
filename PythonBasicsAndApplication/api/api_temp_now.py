import requests

api_url = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Город? ")

params = {
    'q': city,
    'appid': '11c0d3dc6093f7442898ee49d2430d20',
    'units': 'metric',
    'lang': 'ru'
}

res = requests.get(api_url, params=params)
# print(res.status_code)
# print(res.headers['Content-Type'])
data = res.json()  # returns json.loads(res.text)
template = "Температура в городе {} {}"
print(template.format(city, data["main"]["temp"]))
