# for x in [1, 'e', 5]:
#     print(x)


# k = 'Varadero'

# # Введите ваше решение ниже

# value = 0
# k = k.lower()
# print(k)
# dict = {'aeiolnstr': 1, 'dg': 2, 'bcmp': 3,
#         'fhvwy': 4, 'k': 5, 'jx': 8, 'qz': 10}
# for i in k:
#     value += dict[i]
# print(value)
# dict

"""Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
"""

# sl = 'a a a b c a a d c d d'
# sl1 = sl.split()
# print(type(sl),type(sl1))
# print(sl)
# print(sl1)


# string = "a a a b c a a d c d d"    # вводим данные в виде строки
# string_2 = string.split()   # метод возвращает список из введенной строки
# result = {} # задаем пустой словарь
# for i in string_2: # переборка каждого элемента списка
#     if i in result: # если элемент есть в словаре
#         print(f'{i}_{result[i]}', end=' ')  # выводим на экран значение в формате "элемент_значение ключа"
#     else:
#         print(i, end=' ')   # иначе, выводим текущий элемент списка
#     result[i] = result.get(i, 0) + 1    # присваиваем значению ключа i текущее значение этого ключа + 1


"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells

Output: 13
"""

# text = 'She sells sea shells on the sea shore The shells that she sells are sea shells Im sure So if she sells sea shells on the sea shore Im sure that the shells are sea shore shells'
# text = text.upper()
# text1 = text.split()
# print(text1)
# text2 = []
# for i in text1:
#     if i not in text2:
#         text2.append(i)
# print(text2)
# print(len(text2))


"""
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить значение наибольшего элемента
последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до
конца сделать это задание.
Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи
обратились к Вам, студентам.
Примечание: Программные коды на следующих
слайдах"""

# n = int(input('Введите число: ')) # решение не верно
# max_number = 1000
# while n != 0:
#     n = int(input('Введите следующее число: '))
#     if max_number > n:
#         max_number = n
# print(max_number)

# n = int(input('Введите число: ')) # решение не верно
# max_number = -1
# while n < 0:
#     n = int(input('Введите следующее число: '))
#     if max_number < n:
#         n = max_number
# print(n)

# n = int(input('Введите число: '))
# max_number = n
# while n != 0:
#     n = int(input('Введите следующее число: '))
#     if max_number < n:
#         max_number = n
# print(max_number)

