# _author_ = Nikita_Savchenko

with (open('task3text.txt', 'r')) as my_file:
    as_list = my_file.read().split('\n')
    sal_counter = []
    lower_sal = []
    sal_min = 20000
    for i in as_list:
        i = i.split()
        if int(i[1]) < sal_min:
            lower_sal.append(i)
        sal_counter.append(i[1])
    print(f'{lower_sal}')
    print(f'Median sal in comp: {sum(map(int, sal_counter)) / len(sal_counter)}')
my_file.close()


