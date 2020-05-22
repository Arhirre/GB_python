# _author_ = Nikita_Savchenko

from itertools import count

a = int(input('Enter start num: '))
b = int(input('Enter stop num: '))
for num in count(a):
    if num > b:
        break
    else:
        print(num)


