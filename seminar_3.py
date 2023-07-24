# list
# some_list = []
# print(type(some_list))

# some_list = [1, 1.34, 'hello', True, [1,2,3]]
# print(some_list)

# print(some_list[-1])

# print(some_list[2:4])

# print(some_list[:4])

# print(some_list[::-1])


# вводится количество чисел, затем сами числа. Добавить в список только четные числа

# count = int(input('введите количество чисел: '))
# some_list = []
# for _ in range(count):
#     num = int(input('Введите число: '))
#     if num%2==0:
#         some_list.append(num)
# print(some_list)


# some_list = [1, 2, True, 'hello']

# for el in some_list:
#     print(el)        # вариант вывода элементов списка

# for ind in range(0, len(some_list)):
#     print(some_list[ind])                 # вариант вывода элементов списка


                # создание списка со случайными значениями
import random
count = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(count):
    number = random.randint(0, 10)
    some_list.append(number)
print(some_list)


#Создайте список из случайных чисел. Найдите номер его последнего локального максимума
#(локальный максимум — это элемент, который больше любого из своих соседей).
# 1 var
# local_max = None
# for ind in range (0, len(some_list)-1):
#     if some_list[ind-1] < some_list[ind] > some_list[ind+1]:
#         local_max = ind
#         break
# print(local_max)

# 2 var
# import random
# n = int(input('Введите количество элементов: '))
# list = [random.randint(-50, 50) for item in range(n)] # заполнение списка с помощью генератора списков
# print(list)
# local_max = 0
# for i in range(1, len(list) - 1):
#     if list[i] > list[i - 1] and list[i] > list[i + 1]:
#         local_max = list[i]
# print(local_max)
# print(i)



# Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

## создание списка со случайными значениями
# 1 var
# max_count = 0
# for el in some_list:
#     amount = 0
#     for i in some_list:
#         if el == i:
#             amount += 1
#     if amount > max_count:
#         max_count = amount
# print(max_count)

#2 var
# max_count = 0
# for el in some_list:
#     amount = some_list.count(el) # возвращает кол-во элементов el в списке
#     if amount > max_count:
#         max_count = amount
# print(max_count)


"""
Задача №17. 
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

## Создание списка со случайными значениями
# new_list = []
# for el in some_list:
#     if el not in new_list:
#         new_list.append(el)
# print(len(new_list))


"""
Задача №19. 
Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

# k = int(input('Введите число для сдвига: '))
# print(some_list[-k:] + some_list[:-k])


"""
Задача №23.
Дан список, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов списка, больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
"""

# num =  0
# for ind in range(0, len(some_list)-1):
#     if some_list[ind] < some_list[ind+1]:
#         num += 1
# print(num)