# _author_ = Nikita_Savchenko

# elements

ele_int = 1
ele_string = 'Privet'
ele_float = 1.1
ele_list = ['a', '1', 'b', 'c']
ele_tuple = ('a', '1', '1a', [1, 2, 3])
# list

allele_list = [ele_int, ele_string, ele_float, ele_list, ele_tuple]

# script

for i in allele_list:
    print(f'{i} - {type(i)}')
