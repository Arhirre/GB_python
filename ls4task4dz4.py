# _author_ = Nikita_Savchenko
from functools import reduce

print(f'{[ele for ele in range(99, 1001) if ele % 2 == 0]}')


def mult_func(ele,ele_next):
    return ele * ele_next


print(f'{reduce(mult_func,[ele for ele in range(99, 1001) if ele % 2 == 0])}')