import math

action = input("What action would you like to do? (Add, Subtract, Multiply, Divide, Exponent, Square Root.)")
if action == 'Add':
    number1 = float(input('Enter the first number'))
    number2 = float(input('Enter the second number'))
    solution = number1+number2
    print(solution)
elif action == 'Subtract':
    number1 = float(input('Enter the first number'))
    number2 = float(input('Enter the second number'))
    solution = number1-number2
    print(solution)
elif action == 'Multiply':
    number1 = float(input('Enter the first number'))
    number2 = float(input('Enter the second number'))
    solution = number1*number2
    print(solution)
elif action == 'Divide':
    number1 = float(input("Enter the numerator"))
    number2 = float(input("Enter the denominator"))
    solution = number1/number2
    print(solution)
elif action == 'Exponent':
    number1 = float(input('Enter the base number'))
    number2 = float(input('Enter the exponent'))
    solution = number1**number2
elif action == 'Square Root':
    number1 = float(input('Enter the number'))
    solution = math.sqrt(number1)
    print(solution)
elif action == 'sin':
    number1 = math.radians(float(input('Enter the number')))
    solution = math.sin(number1)
    print(solution)
elif action == 'cos':
    number1 = math.radians(float(input('Enter the number')))
    solution = math.cos(number1)
    print(solution)
elif action == 'tan':
    number1 = math.radians(float(input('Enter the number')))
    solution = math.tan(number1)
    print(solution)
else:
    print('Error: input cannot be understood')
