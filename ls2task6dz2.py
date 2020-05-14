# _author_ = Nikita_Savchenko

# new item adding cycle
stockpile = []
while input('Add new item? y/n?: ') == 'y':
    item_num = int(input('Enter item number: '))
# adding characteristics for new items
    characteristics = {}
    while input('Add item characteristics? y/n?') == 'y':
        char_name = input('Enter characteristic name: ')
        char_value = input('Enter characteristic value: ')
        characteristics[char_name] = char_value
    stockpile.append(tuple([item_num, characteristics]))
print(stockpile)

#analitic dict
analitic_dict = {}
for item in stockpile:
    for char_name, char_value in item[1].items():
        if char_name in analitic_dict:
            analitic_dict[char_name].append(char_value)
        else:
            analitic_dict[char_name] = [char_value]
        
        
print(analitic_dict)

