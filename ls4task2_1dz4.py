# _author_ = Nikita_Savchenko
# в заданиях с числовыми листами использовал генератор рандомных чисел для составления

import random

a = int(input('Enter lower end of random numbers generator: '))
b = int(input('Enter higher end of random numbers generator: '))
stop_number = int(input('Enter how many numbers to generate: '))

my_list = [random.randrange(a, b, 1) for i in range(stop_number)]
print(my_list)

my_list_sorted = [ele for num, ele in enumerate(my_list) if my_list[num - 1] < my_list[num]]

print(my_list_sorted)




