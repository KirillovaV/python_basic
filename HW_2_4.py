"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_str = input("Введите строку из нескольких слов через пробел:\n>>>")
word_list = user_str.split(" ")

for el in word_list[:]:
    if not el:
        word_list.remove(el)

if not word_list:
    print("Нет слов для вывода!")
    exit()

for i, el in enumerate(word_list, 1):
    print(i, el[:10])
