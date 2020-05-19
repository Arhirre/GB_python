# _author_ = Nikita_Savchenko

# Через возведение в степень. на всякий случай добавил ввод положительного Y.


# def exponent_func(x, y):
#     if y < 0:
#        exp = 1 / x ** abs(y)
#        return exp
#     elif y > 0:
#         exp = x ** abs(y)
#         return exp
#
#
# print(exponent_func(float(input('Enter X: ')), int(input('Enter Y: '))))


# Через цикл.

def exp_cycle_func(x, y):
    exp = 1
    for i in range(abs(y)):
        exp *= x

    if y < 0:
        return 1 / exp
    elif y >= 0:
        return exp


print(exp_cycle_func(float(input('Enter X: ')), int(input('Enter Y: '))))



