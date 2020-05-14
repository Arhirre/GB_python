# _author_ = Nikita_Savchenko

#  made with list

month_input = int(input('Enter number of the month: '))
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
season_list = ['Winter', 'Spring', 'Summer', 'Fall']
if month_input == 12 or month_input >=1 and month_input <=2:
    print(f'{month_list[month_input-1]} is {season_list[0]}')
elif month_input >=3 and month_input <=5:
    print(f'{month_list[month_input-1]} is {season_list[1]}')
elif month_input >=6 and month_input <=8:
    print(f'{month_list[month_input-1]} is {season_list[2]}')
elif month_input >=9 and month_input <=11:
    print(f'{month_list[month_input-1]} is {season_list[3]}')
else:
    print(f'there is no month with number - {month_input} in year, choose between 1 and 12!')





