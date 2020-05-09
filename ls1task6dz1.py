# _author_ = Nikita_Savchenko

a = int(input('ввелите результат спортсмена в первый день: '))
b = int(input('введите целевой результат спортсмена: '))
progress_mul = 1.1
day = 1
while a < b:
    a = a * 1.1
    day += 1

print(f'спортсмен достиг заданного результата на {day} день')
