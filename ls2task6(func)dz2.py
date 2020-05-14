# _author_ = Nikita_Savchenko

# был знаком с циклами в JS и решил попробовать реализовать тут, т.к лично мне не нравится реализация через while
# а тут я смог добавить возврат при вообще чего либо кроме Y and N.


# ВОПРОС!! после того как я сделал функции добавление в лист через аппенд начало добавлять в список в обратную сторону
# лист выгдяит так [(2, {'Name': 'Printer', 'Price': '3000', 'Size': '30x30'}), (1, {'Name': 'Pc', 'Price': '5000'})]
# что я сделал не так? ( я знаю что совсем скоро разберем циклы на уроке, но если вдруг ответ краткий хотелось бы
# услышать, можно коментом на гите.


stockpile = []
analitic_dict = {}

def item_add_function():
    user_answer = input('add new item? y/n ')
    if user_answer == 'y':
        item_num = int(input('Enter item number: '))
        characteristics = {}
        item_add_char_function(characteristics)
        stockpile.append(tuple([item_num, characteristics]))
    elif user_answer == 'n':
        print(stockpile)
    else:
        item_add_function()


def item_add_char_function(characteristics):
    user_answer = input('add char? y/n ')
    if user_answer == 'y':
        char_name = input('Enter characteristic name: ')
        char_value = input('Enter characteristic value: ')
        characteristics[char_name] = char_value
        item_add_char_function(characteristics)
    elif user_answer == 'n':
        item_add_function()
    else:
        item_add_char_function(characteristics)

def analitic_function(stockpile):
    for item in stockpile:
        for char_name, char_value in item[1].items():
            if char_name in analitic_dict:
                analitic_dict[char_name].append(char_value)
            else:
                analitic_dict[char_name] = [char_value]


item_add_function()
analitic_function(stockpile)
print(stockpile)
print(analitic_dict)