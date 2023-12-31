# Цикл While

# Выведите слово Hello 10 раз

# i = 0
# while i < 10:
#     print ('Hello ')
#     i += 1

# Вводятся числа пока не введут 0. Определите количество четных чисел из введенных

# count = 0
# while True:
#     number = int (input ('input number: '))
#     if number == 0:
#         break
#     if number % 2 == 0:
#         count += 1
# print (count)


# Цикл for

# Переменная-итератор используется

# for i in 'hello':
#     print (i)

# for j in range(5):
#     print(j)

# for j in range(5, 10):
#     print(j)

# for j in range(5, 10, 2):
#     print(j)

# for j in range(10, 5, -1):
#     print(j, end=' ')

# some_str = 'привет мир!'
# for i in some_str:
#     print (i)
# for ind in range(0, len(some_str), 2):
#     print (some_str[ind])

# for ind in range(len(some_str) - 1, -1 , -1):
#     print (some_str[ind])


# Переменная-итератор не используется

# Вывести Hello 10 раз

# for _ in range(10):
#     print ('Hello')

# Вводится количество чисел, затем сами числа. Найти произведение нечетных чисел

# n = int (input())
# q = 1
# for _ in range(n):
#     x = int (input())
#     if x % 2 != 0:
#         q = q * x
# print (q)


# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = int(input("Input number: "))
# count = 1
# q = 1
# if n > 0:
#     while count <= n:
#         q *= count
#         count += 1
#     print (q)
# else:
#     print ('Введено неверное число!')


# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = int (input('Input number: '))
# n1 = 0
# n2 = 1
# temp = n1 + n2
# count = 3
# while a > temp:
#     n1 = n2
#     n2 = temp
#     temp = n1 + n2
#     count += 1
# if temp == a:
#     print (count)
# else:
#     print(-1)


# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# n = int(input('Введите количество дней: '))
# count = 0
# max_count = 0
# for _ in range(n):
# temp = int(input('Введите температуру: '))
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# if count > max_count:
#     max_count = count
# print(max_count)


"""15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""

# n = int (input('Введите количество арбузов: '))
# max_weight = 1
# min_weight = int (input('Введите массу арбуза: '))
# for _ in range(n-1):
#     weight = int (input('Введите массу арбуза: '))
#     if weight > max_weight:
#         max_weight = weight
#     if weight < min_weight:
#         min_weight = weight
# print (min_weight, max_weight)