"""
Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива

Ввод:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1

Вывод:
3 3 2 12
"""

# n = int(input("Input N: "))
# n_set = set()
# for _ in range(n):
#     num = int(input("Input elements of N_set: "))
#     n_set.add(num)
# m = int(input("Input M: "))
# m_set = set()
# for _ in range(m):
#     num = int(input("Input elements of M_set: "))
#     m_set.add(num)

# dif = n_set.difference(m_set)
# print(dif)


# n = int(input('введите количесво символов в первом списке: '))
# list1 = []
# for _ in range (n):
#     list1.append(int(input('введите значение элемента первого списка: ')))
# m = int(input('введите количесво символов в втором списке: '))
# list2 = []
# for _ in range (m):
#     list2.append(int(input('введите значение элемента второго списка: ')))
# print(list1)
# print(list2)

# for el in list1:
#     if el not in list2:
#         print(el, end=' ')


import time
import random

# n = int(input("Input N: "))
# n_set = set()
# for _ in range(n):
#     num = random.randint(1, 10000)
#     n_set.add(num)

# n_list = list(n_set)

# проверка скорости выполнения операций во множестве и в списках

# start = time.perf_counter()
# print(0 in n_set)
# end = time.perf_counter()
# duration_set = end - start

# start = time.perf_counter()
# print(0 in n_list)
# end = time.perf_counter()
# duration_list = end - start

# print(duration_list / duration_set)


"""
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.
Ввод:       Ввод:
5           5
1 2 3 4 5   1 5 1 5 1
Вывод:      Вывод:
0           2
"""

# n = int(input("Input N: "))
# n_list = []
# for _ in range(n):
#     num = random.randint(1, 10)
#     n_list.append(num)
# print(n_list)
# count = 0
# for ind in range(1, n-1):
#     if n_list[ind-1]<n_list[ind]>n_list[ind+1]:
#         count += 1
# print(count)



"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод:           Вывод:
1 2 3 2 3       2
"""

# n = int(input("Input N: "))
# n_list = []
# for _ in range(n):
#     num = random.randint(1, 10)
#     n_list.append(num)
# print(n_list)
# count = 0
# for el in set(n_list):
#     count += n_list.count(el) // 2
# print(count)


# n = int(input('введите количесво символов в первом списке: '))
# list1 = []
# for _ in range (n):
# list1.append(int(input('введите значение элемента первого списка: ')))
# a = set(list1)
# count_res = 0
# for i in a:
# count = 0
# for j in list1:
# if i == j:
# count += 1
# count_res += count // 2
# print(count_res)