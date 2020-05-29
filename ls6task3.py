# _author_ = Nikita_Savchenko


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'Wage': wage, 'Bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income.get('Wage') + self._income.get('Bonus')


worker_one = Position('Nikita', 'Savchenko', 'junior', 35000, 25000)
print(worker_one.get_full_name(),  worker_one.position,  worker_one.get_total_income())


