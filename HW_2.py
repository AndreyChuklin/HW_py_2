'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    *Пример:*
    - 6782 -> 23
    - 0,56 -> 11
'''
# from operator import index


# a = input('Введите любое число: ')
# sum = 0
# print(f'Вы ввели число {a}')

# for i in a:
#     if i != 0:
#         sum += int(i)
# print(f'Сумма чисел равна {sum} от введеного числа {a}')

'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

    - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

# def fact (num, count = 1):
#     for i in range(1, num + 1):
#         count *= i
#     return count

# n = int(input('Введите число: '))
# print(f'Произведение чисел от 1 до {n} = ', end = '')
# for i in range(1, n + 1):
#     if i == n: 
#         print(f'{fact(i)}')
#     else:
#         print(f'{fact(i)}', end = ', ')

'''
3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

    - Для n = 6: 14.07
'''

# from msilib import sequence

# a = int(input('Введите число: ')) 

# def sque(a):
#     return [round((1 + 1 / x)**x, 5) for x in range (1, a + 1)]

# num = sque(a)
# print(num)
# print(round(sum(num), 2))

'''
4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
   Найдите произведение элементов на указанных позициях. 
   Позиции вводятся пользователем с клавиатуры. 5 2 8

   [-5 -4 -3 -2 -1 0 1 2 3 4 5] -> -8
'''

# from random import randint
# nums = []
# for i in range(10):
#     nums.append(randint (-10,10))
# print(nums)

# def numbers(nums):
#     count =0 
#     for element in nums:
#         count +=1
#     return count
# print('Колтчество элементов: ', numbers(nums))

# x = int(input('Введите позицию первого элемента: '))
# y = int(input('Введите позицию второго элемента: '))

# for i in range(len(nums)):
#     multi = nums[x -1]*nums[y - 1]
# print(f'Произведение элементов: {nums[x -1]} * {nums[y -1]} =', multi)

'''
5. Реализуйте алгоритм перемешивания списка.
random.randint(2, 6)
random.randrange(2, 6)
'''
import random
def mix_list(lst_orig):
    lst = lst_orig[:]
    lst_length = len(lst)
    
    for i in range(lst_length):
        ind = random.randint(0, lst_length - 1)
        temp = lst[i]
        lst[i] = lst[ind]
        lst[ind] = temp
    return lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mix_lst = mix_list(lst)
print("Исходный список: ")
print(lst)
print("Перемешанный список: ")
print(mix_lst)