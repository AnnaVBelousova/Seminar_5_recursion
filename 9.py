# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum_of_number(a, b):
    if b==0:
        return a
    else:
        a = a+1
    return sum_of_number(a, b-1)

try:  
    a = int(input("Введите число:"))
    b = int(input("Введите число:"))

    res = sum_of_number(a, b)
    print (res)
except ValueError:
    print ("Это не число!")