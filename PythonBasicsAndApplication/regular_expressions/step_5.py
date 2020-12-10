import re

pattern = r"(test)*"  # для группировки используется метасимвол ()
string = "test"
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 4), match='test'>

pattern = r"(test|text)*"  # метасимвол | означает "или"
string = "testtext"
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 8), match='testtext'>

pattern = r"((abc)|(test|text)*)"  # метасимвол | означает "или"
string = "testtext"
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 3), match='abc'>
print(match.groups())  # ('abc', 'abc', None), вывели значение трех групп. Каждой группе соответствует пара
# открывающей и закрывающей скобки. 'abc' - ((abc)|(test|text)*), первая открывающая скобка == все регулярное выражение;
# 'abc' - (abc), вторая группа, вторая открывающая скобка; None - (test|text), третья группа == третья открывающая
# скобка

pattern = r"((abc)|(test|text)*)"
string = "testtext"
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 8), match='testtext'>
print(match.groups())  # ('testtext', None, 'text'); третьей группе соответствует слово 'text'. Когда мы используем
# группы и метасимвол повторения, запоминаетя последнее вхождение

pattern = r"Hello (abc|test)"
string = "Hello abc"
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 9), match='Hello abc'>
print(match.group(0))  # Hello abc; получаем все совпадение целиком. Для group 0 - значение по умолчанию
print(match.group(1))  # abc; получаем содержимое первой открывающей скобки и группы которая ей соответствует

pattern = r"(\w+)-\1"  # \w+ - объединяем несколько, подряд идущих буквенных символов в одну группу, а затем,
# с помощью \1 ищем группу, уже собранную ранее. Номер после слеша соответствует номеру группы
string = "test-test"
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 9), match='test-test'>

pattern = r"(\w+)-\1"
string = "test-test chow-chow"
duplicates = re.sub(pattern, r'\1', string)  # используя собранную группу, оставляем только то, что соответствует "\1".
# Важно использовать сырую строку
print(duplicates)  # test chow
inclusions = re.findall(pattern, string)
print(inclusions)  # ['test', 'chow']  при использовании групп функция findall возвращает кортеж групп
# вместо подстрок целиком

pattern = r"((\w+)-\2)"  # используем вместо одной группы две, ловим всю строку целиком, меняем цисло после \ на 2
string = "test-test chow-chow"
inclusions = re.findall(pattern, string)
print(inclusions)  # [('test-test', 'test'), ('chow-chow', 'chow')]
