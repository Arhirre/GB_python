# _author_ = Nikita_Savchenko
import re

my_dict = {}
with open('task6text.txt', 'r') as my_file:
    for l in my_file:
        subject, lecture, practice, lab = l.split()
        str_list = re.split("(\d+)", l)
        only_nums = [x for x in str_list if x.isdigit()]
        only_nums_int = list(map(int, only_nums))
        my_dict[subject] = sum(only_nums_int)
    print(my_dict)
