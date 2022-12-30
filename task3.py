# Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ), применив лямбды, filter, map,
# zip, enumerate, списочные выражения.

# №1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # 6782 -> 23
# # 0.56 -> 11
#
# print("Введите вещественное число\n")
# str = input()
# #             БЫЛО:
# # summa = 0
# # number = []
# # for i in range(len(str)):
# #     if str[i].isdigit():
# #         summa += int(str[i])
# # print("Сумма цифр числа = ", summa)
#
# # list = [sum += int(str[i]) for i in str if i.isdigit()]
# #             СТАЛО:
# number = str.replace('.','')
# number = [int(i) for i in number]
# print("Сумма цифр числа = ", sum(number))


#   №2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#               БЫЛО:
# count = 1
#
# print("Введите  число N \n")
# n = int(input())
# for i in range(1, n+1):
#     count = count * i
#     print(count, end=' ')

#                 СТАЛО:
# n = int(input("Введите  число N "))
# sp = [i for i in range(1, n+1)]
# sp = list(map(lambda x: math.factorial(x), sp))
# print(sp)