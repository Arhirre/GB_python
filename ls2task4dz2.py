# _author_ = Nikita_Savchenko

user_str = input('Enter string: ')

x = user_str.split(' ')
for i, ele in enumerate(x, 1):
    if len(ele) > 10:
        ele = ele[0:10]
    print(f'{i}) {ele}')

