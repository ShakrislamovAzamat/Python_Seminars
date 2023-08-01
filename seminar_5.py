"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется последовательность чисел
a0, a1, ..., an, ..., где
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
"""


# def fib(n): # вызов ф-ции через рекрсию
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n-1) + fib(n-2)


# def fib_cycle(n): # вызов ф-ции через цикл
#     if n == 0:
#         return 0
#     elif n in [1,2]:
#         return 1
#     first = 1
#     second = 1
#     temp = first + second
#     count = 3
#     while count < n:
#         first = second
#         second = temp
#         temp = first + second
#         count += 1
#     return temp


# import time
# start = time.perf_counter() # засекаем время начала ф-ции
# print(fib(30))
# end = time.perf_counter() # засекаем время окончания ф-ции
# duration1 = end - start # время выполнения ф-ции

# start = time.perf_counter() #
# print(fib_cycle(30))
# end = time.perf_counter() #
# duration2 = end - start #

# print(duration1 / duration2) # отношение времени вып-я первой ф-ции ко времени вып-я второй ф-ции



"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 4 8 9 1 2
Output: 4 8 1 1 2
"""

# list_1 = [4, 8, 9, 1, 2, 5, 9, 6, 9]

# print(list_1) # решение через цикл
# max_ = max(list_1)
# min_ = min(list_1)
# for ind in range(len(list_1)):
#     if list_1[ind] == max_:
#         list_1[ind] = min_

# print(list_1)


# def change_marks (list_1): # решение рекурсивным методом
#     max_ = max(list_1)
#     min_ = min(list_1)
#     list_1[list_1.index(max_)] = min_
#     if max_ not in list_1:
#         return list_1
#     return change_marks(list_1)

# print(change_marks(list_1))


"""
Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
"""


n = 23

# def simple (n, div): # рекурсия
#     if div == 1:
#         return True
#     if n % div == 0:
#         return False
#     return simple(n, div-1)

# print(simple(n, n//2 + 1))


# for div in range(2, n//2+1):
#     if n % div == 0:
#         print('no')
#         break
# else:
#     print('yes')



"""
Задача №37. Решение в группах
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""

# def change(n):
#     if n == 0:
#         return ''
#     num = int(input())
#     return change(n-1)+f'{num} '

# n= int(input('Введите число = '))
# print(change(n))


