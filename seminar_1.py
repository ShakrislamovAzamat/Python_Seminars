# https://github.com/ZeeMix/13072023
# https://www.jetbrains.com/ru-ru/pycharm/download/?section=windows
# @WoT_Master


# print('Hello world!')

# name = input('Введите имя: ')
# surname = input ('Введите фамилию: ')
# print ('Здравствуйте, ' + name + ' ' + surname)
# print ('Здравствуйте,', name, surname)
# print (f'Здравствуйте, {name} {surname}')

# a = 'Hello'
# print(type(a), a)
# b = 123
# print(type(b), b)
# c = 12.3
# print(type(c), c)
# d = True
# print(type(d), d)


# a = 15
# b = 7

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)

# print(a<b)
# print(a>b)
# print(a==b)
# print(a!=b)


# a = int(input('Введите число: '))
# if a>0:
#     if a%2==0:
#         print(f'Число {a} четное положительное')
#     else:
#         print(f'Число {a} нечетное положительное')
# elif a==0:
#     print(f'Число {a} равно 0')
# if a%2==0:
#     print(f'Число {a} четное отрицательное')
# else:
#     print(f'Число {a} нечетное отрицательное')


"""Задача 1
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2"""

# n = int(input())
# m = int(input())
# # print(m//n + 1 % (m % n + 1))
# print((-m)//n*(-1))


"""Задача №3. Решение в группах
В некоторой школе решили набрать три новых
математических класса и оборудовать кабинеты для
них новыми партами. За каждой партой может сидеть
два учащихся. Известно количество учащихся в
каждом из трех классов. Выведите наименьшее
число парт, которое нужно приобрести для них.
Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32"""

# a = 20
# b = 22
# c = 21
# x = (a%2+a//2)+(b%2+b//2)+(c%2+c//2)
# print(x)

# print(((-(a))//2 * -1)+((-(b))//2 * -1)+((-(c))//2 * -1))


"""Дано натуральное число. Требуется определить,
является ли год с данным номером високосным. Если
год является високосным, то выведите YES, иначе
выведите NO. Напомним, что в соответствии с
григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400.
Input: 2016
Output: YES"""

# y = int(input("Введите год: "))
# if y%4==0 or y%400==0 and y%100!=0:
#     print('YES')
# else:
#     print ('NO')