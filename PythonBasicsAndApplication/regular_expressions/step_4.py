import re

pattern = r"ab*a"
string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aa', 'aba', 'abba'] * любое число символов, включая 0

pattern = r"ab+a"
string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aba', 'abba'] + любое число положительных символов(0 не входит)

pattern = r"ab?a"
string = "aa, aba, abba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aa', 'aba'] ? 0 или одно вхождение символа

pattern = r"ab{3}a"
string = "aa, aba, abba, abbba, abbbba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abbba'] {3} число символов в фигурных скобках(3)

pattern = r"ab{2,4}a"
string = "aa, aba, abba, abbba, abbbba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abba', 'abbba', 'abbbba'] {2,4} от двух до четырех вхождений

pattern = r"a[ab]+a"
string = "abaaba"
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 6), match='abaaba'>, [ab]+ собирает в себя все символы, удовлетворяющие
# условию, затем проверяет остаток строки и при необходимости забирает символы из конца [ab]+
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abaaba']

pattern = r"a[ab]+?a"
string = "abaaba"
match = re.match(pattern, string)
print(match)  # <re.Match object; span=(0, 3), match='aba'>
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aba', 'aba'] - [ab]+? знак вопроса после плюса - поиск наименьшего числа выражений,
# удовлетворяющих регулярному выражению
