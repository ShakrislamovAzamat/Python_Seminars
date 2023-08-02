"""
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15
"""

# def  arprog (a, d, n):
#     newlist = []
#     for i in range(1, n+1):
#         newlist.append(a + (i - 1) * d)
#     return newlist

# a = int(input('Input first element: '))
# d = int(input('Input differential: '))
# n = int(input('Input number of elements: '))
# print(arprog(a, d, n))


"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)

Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
"""

# import random
# new = []
# for _ in range (20):
#     new.append(random.randint(-20, 20))
# print(new)

# def select(lst, min_value, max_value):
#     new = []
#     for i in range(len(lst)):
#         if min_value <= lst[i] <= max_value:
#             new.append(i)
#     return new

# min_value = int(input('Input minValue: '))
# max_value = int(input('Input maxValue: '))
# print(select(new, min_value, max_value))