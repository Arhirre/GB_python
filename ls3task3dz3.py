# _author_ = Nikita_Savchenko


def my_func(x, y, z):
    num_list = [x, y, z]
    num_max1 = max(num_list)
    num_list.remove(num_max1)
    num_max2 = max(num_list)
    print(num_max1 + num_max2)


my_func(2, 4, 3)
