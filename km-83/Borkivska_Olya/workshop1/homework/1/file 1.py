"""
Функція, яка має 2 числа і обчислює скльки % перше число складає від другого
"""
def calc():
    first_number = int((input("Enter 1st number: ")))
    second_number = int((input("Enter 2nd number: ")))
    x = (second_number * 100) / first_number
    return x

print(calc())

