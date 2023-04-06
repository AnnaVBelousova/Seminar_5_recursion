# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def power(A,B):
    if B == 1:
        return A
    else:         
        return A *power (A,B-1)
    
try:
    A = int(input("Введите число:"))
    B = int(input("Введите число:"))
   
    res = power(A,B)
    print(res)

except ValueError:
    print ("Это не число!")
