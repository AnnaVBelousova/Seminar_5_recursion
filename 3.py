



def invert_number(N, lst = []):

      last = N%10
      lst.append(last)
      invert_number_as_string = ''.join(map(str,lst))
      invert_number_as_string.replace(' ','')
      
      if  N//10==0:
          return invert_number_as_string
      
      return  invert_number(N//10, lst)

try:
    N = int(input("Введите число:"))
    res = invert_number(N, lst = [])
    print(res)
    
except ValueError:
    print("Это не число!")
