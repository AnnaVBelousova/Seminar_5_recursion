



def summa_of_numbers(n, lst = []):

    if n-1 == -1:
        return sum(lst)
    else:
        lst.append(n)
    return summa_of_numbers(n-1, lst) 

try:
    n = int(input("Введите число:"))
    res = summa_of_numbers(n, lst = [])
    print (res)

    checkout = n*(n+1)/2

    if  checkout == res:
        print("Равенство выполняетcя")
    else :
        print("Равенство не выполняется")
except ValueError:
    print ("Это не число!")