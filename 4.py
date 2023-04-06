# Задание 4. Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
# Пример:
# Введите количество элементов: 3
# Количество элементов - 3, их сумма - 0.75
# Решите через рекурсию. В задании нельзя применять циклы.
# Нужно обойтисть без создания массива!


def sum_of_element( number, count=0 ):
      
    if  number!=0:
        
        if (number-1)%2==0:
            count = count+(1/2**(number-1))
            #print (1/2**(number-1))
        else: 
            count = count+(1/2**(number-1))*(-1)
            #print (count)
        return sum_of_element( number-1, count)
       
    else: 
        if number == 0:
            return count
        
try:
    number = int(input("Введите число:")) 
    res = sum_of_element(number, count = 0)
    print(res)
except ValueError:
    print("Это не число!")