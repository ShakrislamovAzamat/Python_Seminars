"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""

# n = int(input('Введите количество монет: '))
# minimal = 0
# count_0 = 0
# count_1 = 0
# for _ in range(n):
#     coin = int(input('Введите сторону монеты (0 - решка, 1 - герб): '))
#     if coin > 0:
#         count_1 += 1
#     else:
#         count_0 += 1
# if count_0 > count_1:
#     print(count_1)
# else:
#     print(count_0)


"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""

# s = int(input('Введите сумму чисел: '))
# p = int(input('Введите произведение чисел: '))
# for i in range(1000):
#     x = i
#     for j in range(i):
#         y = j
#         if x * y == p and x + y == s:
#             print(x, y)


"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2k), не превосходящие числа N.
"""

# n = int(input('Введите число N: '))
# k = 0
# while 2**k <= n:
#     print (2**k, end=' ')
#     k += 1