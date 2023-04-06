


 

def operations_with_numbers():

    operator = input("Введите знак операции +, -, *, /, 0:")

    if operator == "0":
        print("Программа завершена")
        return    
    else:
        if operator in '+ - * /': 
            try:
                n1 = int(input("Введите число:"))
                n2 = int(input("Введите число:"))
            except ValueError:
                print("Это не число!")
                operations_with_numbers()

            if operator == '+':
                answer = n1+n2
                print(f'Ваш результат {answer}')
                return operations_with_numbers()
               
            elif operator == "-":
                answer = n1-n2
                print(f'Ваш результат {answer}')
                return operations_with_numbers()
            
            elif operator == "*":
                answer = n1 * n2
                print(f'Ваш результат {answer}')
                return operations_with_numbers()
            
            elif operator == "/":

                try:
                    answer = n1 / n2
                    print(f'Ваш результат {answer}')
                    return operations_with_numbers()
                                   
                except ZeroDivisionError:
                    print("На ноль делить нельзя!")
        else: 
            print("Неверный знак!")

    return operations_with_numbers()

operations_with_numbers()     
 
