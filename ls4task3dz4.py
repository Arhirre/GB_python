# _author_ = Nikita_Savchenko


import random

a = int(input('Enter lower end of random numbers generator: '))
b = int(input('Enter higher end of random numbers generator: '))
stop_number = int(input('Enter how many numbers to generate: '))

my_list = [random.randrange(a, b, 1) for i in range(stop_number)]
print(my_list)

my_list_sorted = [ele for ele in my_list if my_list.count(ele) < 2]
print(my_list_sorted)
