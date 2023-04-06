

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
