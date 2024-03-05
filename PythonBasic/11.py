print('Enter two numbers. I will divide them')
x = int(input('First number: '))
y = int(input('Second number: '))

try:
    result = x / y
except ZeroDivisionError:
    print('You cant divide by zero!')
else:
    print(result)




















