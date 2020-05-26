# _author_ = Nikita_Savchenko

with open('task2text.txt', 'r') as my_file:
    file_lines_count = my_file.readlines()
    print(f'File lines count = {len(file_lines_count)}')
my_file.close()

with open('task2text.txt', 'r') as my_file:
    for i in range(len(file_lines_count)):
        file_line = my_file.readline()
        file_words_per_line = file_line.split()
        print(f'In line words = {len(file_words_per_line)}')
my_file.close()





