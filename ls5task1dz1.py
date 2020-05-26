# _author_ = Nikita_Savchenko

with open('task1.txt', 'w') as my_file:
    string = input('Enter data: ')
    while string:
        my_file.writelines(string + '\n')
        string = input('Enter more data: ')
        if not string:
            break
my_file.close()


