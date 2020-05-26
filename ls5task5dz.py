# _author_ = Nikita_Savchenko


# Цикл- считает сумму в введенной строке и во всем файле целиком, пустая строка - конец ввода.
with (open('task5text.txt', 'w')) as my_file:
    line_sum_holder = []
    string = input('Enter nums sep with spaces: ')
    while string:
        my_file.writelines(string + '\n')
        nums_line = string.split()
        sum_line = sum(map(int, nums_line))
        line_sum_holder.append(sum_line)
        print(f'Sum in current line = {sum_line}')
        print(f'Sum in file total = {sum(map(int, line_sum_holder))}')
        string = input('Enter more nums: ')
        if not string:
            break

my_file.close()


