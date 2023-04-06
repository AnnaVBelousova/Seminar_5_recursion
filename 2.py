






def count_numbers (N, even=0, odd=0):
    if N % 10 % 2 == 0:
        even +=1
    else: odd +=1
    if N//10 == 0:
        return even, odd
    return count_numbers (N//10, even, odd) 

try:
    N = int(input("Введите число:"))
    result = count_numbers(N)
    print(result)
except ValueError:
    print("Это не число!")