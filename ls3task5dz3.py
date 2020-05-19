# _author_ = Nikita_Savchenko


def sum_list():
    total_sum = 0
    while_state = True
    while while_state == True:
        num_list = input('Enter numbers, or * to end: ').split()
        sum_num_list = 0
        for ele in range(len(num_list)):
            if num_list[ele] == '*':
                while_state = False
                break
            else:
                sum_num_list = sum_num_list + int(num_list[ele])
        total_sum = total_sum + sum_num_list
        print(sum_num_list)
        print(total_sum)


sum_list()












