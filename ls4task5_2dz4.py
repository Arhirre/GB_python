# _author_ = Nikita_Savchenko


from itertools import cycle
my_list = [1, 'abcd', 'qwe123', 'nvcx']
list_buffer = cycle(my_list)
repeat = 0
repeat_stop = int(input('Enter how many strings you want to see: '))
for output in list_buffer:
    print(output)
    repeat += 1
    if repeat > repeat_stop - 1:
        break



