# some_list = ['1', '2', '3'] #список текстовых значений

# for i in range(0, len(some_list)): # преобразование значений списка в числа
#     some_list[i]=int(some_list[i])

# print(some_list)

# new_list = list(map(int, some_list))  # преобразование значений списка в числа
# print(new_list)

# some_list = [1, 2, 3]

# for i in range(len(some_list)): # возведение в степень элементов списка
#     some_list[i]=some_list[i]**3
# print(some_list)

# def func(x):
#     return x**3

# new_list = list(map(func, some_list)) # возведение в степень элементов списка
# print(new_list)


#lambda

# new_list = list(map(lambda x: x**3, some_list))
# print(new_list)


#filter

# some_list = [1, 2, 3, 4]

# new_list = []

# for el in some_list:
#     if el % 2 == 0:
#         new_list.append(el)

# print(new_list)

# new_list = list(filter(lambda x: x % 2 == 0, some_list))

# print(new_list)



"""
Задача №47. Решение в группах
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.

"""

# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# print(transormed_values)

"""
Задача №49. Решение в группах
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
"""

# def find_farthest_orbit(orbits):
#     # s_list = [i[0] * i[1] for i in orbits if i[0] != i [1]] # вариант 1
#     # s_max = s_list.index(max(s_list))
#     # return orbits[s_max]
#     maxx = orbits[0]                                          # вариант 2
#     for el in orbits:
#         if el[0] != el[1] and el[0] * el[1] > maxx[0] * maxx[1]:
#             maxx = el
#     return maxx


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))



"""
Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод: 
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
print('same')
else:
print('different')
Вывод: same
"""

# def same_by(characteristic, objects):
#     new_objects = list(filter(characteristic, objects))
#     if len(new_objects) == len(objects) or len(new_objects) == 0:
#         return True
#     return False

# values = [0, 1, 10, 6] 
# if same_by(lambda x: x % 2, values):
#     print("same")
# else:
#     print("different")