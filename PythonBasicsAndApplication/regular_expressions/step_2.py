import re

pattern = r"abc"
string = "abc"
match_object = re.match(pattern, string)
print(match_object)  # <re.Match object; span=(0, 3), match='abc'>  match - показывает вхождение шаблона внутрь строки.
# span - показывает с какой по какую позицию содержится вхождение шаблона в строку
string = "babcde"  # None
pattern = "a[abc]c"  # в квадратных скобках перечисляются символы, которые подходят под шаблон на этой позиции
# при запросе match подойдут строки "aac", "abc", "acc" и т.д.
string = "abc, aac, acc"
first = re.search(pattern, string)
print(first)  # <re.Match object; span=(0, 3), match='abc'> находит первое вхождение строки, подходящей под шаблон

all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abc', 'aac', 'acc'] # findall находит все подстроки, подходящие под шаблон

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)  # abc, abc, abc исправляет все вхождения шаблона согласно аргументу
