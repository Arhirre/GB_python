# _author_ = Nikita_Savchenko

#  made with dict

month_input = int(input('Enter number of the month: '))
month_dict = {
    1: {'name': 'Jan', 'season': 'Winter'},
    2: {'name': 'Feb', 'season': 'Winter'},
    3: {'name': 'Mar', 'season': 'Spring'},
    4: {'name': 'Apr', 'season': 'Spring'},
    5: {'name': 'May', 'season': 'Spring'},
    6: {'name': 'Jun', 'season': 'Summer'},
    7: {'name': 'Jul', 'season': 'Summer'},
    8: {'name': 'Aug', 'season': 'Summer'},
    9: {'name': 'Sep', 'season': 'Fall'},
    10: {'name': 'Oct', 'season': 'Fall'},
    11: {'name': 'Nov', 'season': 'Fall'},
    12: {'name':'Dec', 'season': 'Winter'}
    }
if month_input >=1 and month_input <= 12:
    print(f'{month_dict[month_input]} ')
else:
    print(f'there is no month with number - {month_input} in year, choose between 1 and 12!')

