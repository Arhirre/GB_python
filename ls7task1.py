# _author_ = Nikita_Savchenko


class Matrix:
    def __init__(self, list_1, list_2):
        self.m1 = list_1
        self.m2 = list_2

    def __str__(self):
        # Для вывода всех матриц в привычном виде, можно сделать цикл или же запрос о том какую матрицу вывести.
        # В качестве примера вывожу только первую заданную пользователем.
        return str('\n'.join(['\t'.join([str(i) for i in s]) for s in self.m1]))

    def __add__(self):
        matrix = [[self.m1[s][i] + self.m2[s][i] for i in range(len(self.m1[0]))] for s in range(len(self.m1))]
        return str('\n'.join(['\t'.join([str(i) for i in s]) for s in matrix]))


matr = Matrix([[1, 2, 3],
               [1, 2, 3],
               [2, 2, 2]],
              [[3, 2, 1],
               [3, 2, 1],
               [2, 2, 2]])


print(matr.__str__())
print(matr.__add__())