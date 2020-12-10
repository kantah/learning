from xml.etree import ElementTree

tree = ElementTree.parse('example.xml')  # parse возвращает дерево
root = tree.getroot()
# root = ElementTree.fromstring("example.xml")
# print(root)  # <Element 'studentsList' at 0x000001AF15528EA0>
# print(root.tag, root.attrib)  # studentsList {}

"Можно перебрать детей внутри root с помощью цикла for"
# for child in root:
#     print(child.tag, child.attrib)
# student {'id': '1'}
# student {'id': '2'}

"Для того чтобы обращаться к детям и детям детей можно использовать индексацию через числа"
# print(root[0][0].text)  # Greg

"Для поиска информации внутри элемента можно использовать метод iter"
# for element in root.iter('scores'):
#     print(element)
# <Element 'scores' at 0x000001AF03EF8040>
# <Element 'scores' at 0x000001AF03EF82C0>

for element in root.iter('scores'):  # с помощью iter мы смогли перебрать все элементы в поддереве, findall
    # вернул бы только детей
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
    print(score_sum)
# 240.0
# 240.2


