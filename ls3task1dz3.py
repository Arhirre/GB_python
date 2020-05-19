# _author_ = Nikita_Savchenko

def div_func(x, y):
    try:
        z = x / y
        print(z)
    except ZeroDivisionError:
        print('you cant divide by zero')

div_func(int(input('Enter num, that will be divided - x: ')), int(input('Enter num, that will be divided by - y: ')))