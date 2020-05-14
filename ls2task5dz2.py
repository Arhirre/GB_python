# _author_ = Nikita_Savchenko

user_rating = int(input('Enter your rating elemnt: '))
my_list = [7, 5, 3, 3, 2]
for ele in my_list:
    i = my_list.index(ele)
    if user_rating > ele:
        my_list.insert(i, user_rating)
        break
    elif user_rating < my_list[len(my_list) - 1]:
        my_list.append(user_rating)

print(my_list)

# не совсем понимаю как реализовать 
# :" Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них."
# точнее каким образом я могу отследить что, допустим 3ка которую я добавлю пойдет в конец ряда троек а не в начало или середину, и допустим какой в этом смысл,
# если значения и так одинаковы, а все числа идущие после добавленного съезжают на 1 по индексу?.
