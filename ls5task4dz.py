# _author_ = Nikita_Savchenko

names_match = {'One': 'Odin',
               'Two': 'Dwa',
               'Three': 'Tri',
               'Four': 'Chetre'}

with open('task4text_input.txt', 'r') as my_file:
    my_file_new = []
    for i in my_file:
        i = i.split(' ')
        my_file_new.append(names_match[i[0]] + ' — ' + i[2])
my_file.close()

with open('task4text_output.txt', 'w') as my_file:
    my_file.writelines(my_file_new)
my_file.close()


