# Конструкция in проверяет, входит ли одна строка в другую
s = "abcabc"
print("abc" in s)  # True

# Метод find показывает индекс первого вхождения подстроки в строку
print("abcabc".find("bca"))  # 1

# Если подстрока отсутствует в строке выведется -1
print("abcabc".find("bce"))  # -1

# Метод index делает тоже самое, что и find, но если подстрока отсутствует в строке бросает ошибку ValueError
print("abcabc".index("bce"))  # ValueError: substring not found

# Метод startswith проверяет, ничинается ли строка с другой строки
s = "abcabc"
print(s.startswith("ab"))  # True

# У этих методов есть необязательные скрытые параметры start и end, позволяющие вести поиск на определенном срезе
# строки
# Метод startswith принимает в качестве префикса кортеж значений. В этом случае True возвращается, если
# строка начинается с любого элемента кортежа.
s = "abcabcabc"
print(s.startswith(("ab", "bc", "ca")))   # True

s = "bcabcabc"
print(s.startswith(("ab", "bc", "ca")))  # True

s = "cabcabc"
print(s.startswith(("ab", "bc", "ca")))  # True

# Метод endswith проверяет, заканчивается ли строка подстрокой. С помощью этого метода удобно проверять
# расширения файлов
s = "image.png"
print(s.endswith(".png"))  # True

# Метод count выводит количество непересекающихся вхождений подстроки в строку
s = "abcabcabc"
print(s.count("abc"))  # 3

# Метод rfind работает также, как find, но поиск ведется справа-налево
s = "abcabcabc"
print(s.rfind("ca"))  # 5
