from lxml import etree
import requests

res = requests.get("https://docs.python.org/3/")
print(res.status_code)
print(res.headers["Content-Type"])
# 200
# text/html

parser = etree.HTMLParser()  # HTMLParser позволяет работать с данными в формате HTML
root = etree.fromstring(res.text, parser)
for element in root.iter("a"):  # перебираем все элементы в поддереве, которые являются атрибутом "а"
    print(element, element.attrib)
# <Element a at 0x26834a71d00> {'href': 'genindex.html', 'title': 'General Index', 'accesskey': 'I'}
# <Element a at 0x26834a71e80> {'href': 'py-modindex.html', 'title': 'Python Module Index'}
# <Element a at 0x26833ef7600> {'href': 'https://www.python.org/'}
# <Element a at 0x26834a71d00> {'href': '#'}
# ...
