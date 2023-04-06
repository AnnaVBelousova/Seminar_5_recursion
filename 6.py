# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

from random import randint

number = randint(0, 100)
#print(number)

def what_is_number(k):
   
    if k == 0:
        print("Ваши попытки закончились")
        return (number)
    else:
        if k!=0:
            try:
                N = int(input("Введите число:"))
                if N<number:
                    print("число меньше заданного")
                elif N==number:
                    print("Угадали!")
                    return number   
                else: 
                    print("число больше заданного")
            except ValueError:
                print("Это не число!")

    return what_is_number( k-1)  
         
res = what_is_number(10)
print(res)