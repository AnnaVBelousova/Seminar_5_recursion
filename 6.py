

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