from xml.etree import ElementTree

# tree = ElementTree.parse('example.xml')

'Запись данных xml в файл'
# tree.write('example_copy.xml')

'Изменение значения элемента'
# root = tree.getroot()
# greg = root[0]
# module1 = next(greg.iter('module1'))
# # print(module1, module1.text)  # <Element 'module1' at 0x0000020F455E60E0> 70
# module1.text = str(float(module1.text) + 30)  # увеличиваем значение элемента module1 на 30
# tree.write("tree_modified.xml")  # создаем новый файл и записываем в него измененное дерево

"Добавление нового атрибута элемента"
tree = ElementTree.parse("tree_modified.xml")
root = tree.getroot()
greg = root[0]
# certificate = greg[2]
# certificate.set("type", "with distinction")  # создаем атрибут 'type' с значением 'with distinction'
# tree.write("tree_modified.xml")  # <certificate type="with distinction">True</certificate>

"Добавление нового элемента"
# description = ElementTree.Element('description')  # создаем новый элемент
# description.text = 'Showed excellent skills during the course'  # Записываем текстовое значение для элемента
# greg.append(description)  # добавляем элемент в конец элемента-родителя
# tree.write("tree_modified.xml")  # <description>Showed excellent skills during the course</description></student>

"Удаление элемента"
description = greg.find("description")  # находим первое вхождение элемента с тегом 'description'
greg.remove(description)  # Удаляем найденный элемент
tree.write("tree_modified.xml")  # Записываем изменения в файл

"Создание дерева файла в формате xml"
root = ElementTree.Element("student")  # создаем корень
first_name = ElementTree.SubElement(root, "firstName")  # создаем субэлементы
first_name.text = "Greg"  # задаем текстовое значение
# ...
tree = ElementTree.ElementTree(root)
tree.write("student.xml")
