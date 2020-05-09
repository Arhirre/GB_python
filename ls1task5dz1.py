# dz - Nikita_Savchenko

revenue = int(input('введите значение выручки: '))
costs = int(input('введите значение издержек: '))
profitability = revenue // costs

if revenue > costs:
    print('отлично, ваша фирма не убыточна!')
    print(f'рентабильность выручки {profitability}')
    num_of_workers = int(input('введите кол-во работников фирмы: '))
    profitability_per_worker = (revenue - costs) // num_of_workers
    print(f'прибыль фирмы из расчета на 1 работника: {profitability_per_worker}')
elif revenue <= costs:
    print('Все полимеры кончились :с. Компания работает в убыток')
