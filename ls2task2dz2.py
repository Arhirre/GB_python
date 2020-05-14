# _author_ = Nikita_Savchenko

# ask for list
x =  int(input('set list len: '))
my_list = []
for i in range(x):
    userInput = input('add to the list: ')
    my_list.append(userInput)

# ele swap

if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        ele_holder = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = ele_holder
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        ele_holder = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = ele_holder
        i += 2

print(my_list)












