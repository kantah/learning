import re

x = re.match(r'text', 'TEXT', re.IGNORECASE)  # установив флаг IGNORECASE, игнорируем регистр
print(x)  # <re.Match object; span=(0, 4), match='TEXT'>

x = re.match(r'(te)*xt', 'TEXT', re.IGNORECASE | re.DEBUG)  # чтобы добавить один флаг к другому, используем битовое
# "или"
print(x)
'''
MAX_REPEAT 0 MAXREPEAT  # т.к. мы применили *, мы пытаемся найти максимальное вхождение
  SUBPATTERN 1 0 0  # группа (te) выделилась в subpattern
    LITERAL 116  # каждому буквенному выражению соответствует код в таблице юникода
    LITERAL 101
LITERAL 120
LITERAL 116
 0. INFO 4 0b0 2 MAXREPEAT (to 5)
 5: REPEAT 11 0 MAXREPEAT (to 17)
 9.   MARK 0
11.   LITERAL_UNI_IGNORE 0x74 ('t')
13.   LITERAL_UNI_IGNORE 0x65 ('e')
15.   MARK 1
17: MAX_UNTIL
18. LITERAL_UNI_IGNORE 0x78 ('x')
20. LITERAL_UNI_IGNORE 0x74 ('t')
22. SUCCESS
<re.Match object; span=(0, 4), match='TEXT'>
'''
x = re.match(r'(te)*?xt', 'TEXT', re.IGNORECASE | re.DEBUG)  # если поставить после * метасимвол ?, будет искаться
# минимальное выражение, соответсвующее регулярному выражению
# MIN_REPEAT 0 MAXREPEAT
