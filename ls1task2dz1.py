# dz - Nikita_Savchenko

timeSec = int(input('введите время в секундах: '))
hour = timeSec // 3600
res = timeSec % 3600
minute = res // 60
second = res % 60

print(f'время в формате чч:мм:сс -- {hour}:{minute}:{second}')
