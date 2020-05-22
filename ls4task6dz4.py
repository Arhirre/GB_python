from itertools import count
from math import factorial


def fact(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
        yield x


for ele in fact(int(input('Enter N for  N!: '))):
    print(ele)

