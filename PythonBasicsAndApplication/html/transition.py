"""
Рассмотрим два HTML-документа A и B. Из A можно перейти в B за один переход, если в A есть ссылка на B,
т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега. Из A можно перейти в B за
два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за
один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
"""
import requests
import re

a = requests.get(input())
b = input()
pattern = r"https?://[^\"\s>]+"
a_urls = re.findall(pattern, a.text)
all_urls = []
for url in a_urls:
    url = requests.get(url)
    url_urls = re.findall(pattern, url.text)
    all_urls.extend(url_urls)
if b in all_urls:
    print("Yes")
else:
    print("No")
