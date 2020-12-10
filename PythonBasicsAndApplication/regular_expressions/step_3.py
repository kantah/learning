import re

pattern = r" english?"
string = "Do you speak english?"
match = re.search(pattern, string)
print(match)  # <re.Match object; span=(12, 20), match=' english'> знак вопроса считался как метасимвол

pattern = r" english\?"
string = "Do you speak english?"
match = re.search(pattern, string)
print(match)  # <re.Match object; span=(12, 21), match=' english?'> чтобы ? считался как вопросительный знак,
# его надо экранировать с помощью обратного слеша

pattern = "a[a-zA-Z]c"  # с помощью дефиса задается диапазон. В данном примере подходит любая буква латинского алфавита

pattern = "a[^a-zA-Z]c"  # символ ^(карет, крышечка) показывает, какие символы нам не подходят

# . ^ $ * + ? {} [] \ | ()  # метасимволы

# Т.к. некоторые группы символов используются довольно часто, для них существует короткая запись.
# \d ~ [0-9] -- цифры
# \D ~ [^0-9]
# \s ~ [ \t\n\r\f\v] -- пробельные символы
# \S ~ [^ \t\n\r\f\v]
# \w ~ [a-zA-Z0-9_] -- буквы+цифры+_
# \W ~ [^a-zA-Z0-9_]

pattern = "a[\w.]c"  # дополнили последовательность \w точкой

# под символ . подходит любой символ кроме переноса строки
