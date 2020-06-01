# _author_ = Nikita_Savchenko


class BioCells:
    def __init__(self, q_cells):
        self.q = int(q_cells)

    def __str__(self):
        return f'Result {self.q * "*"}'

    def __add__(self, other):
        return BioCells(self.q + other.q)

    def __sub__(self, other):
        return BioCells(int(self.q - other.q)) if (self.q - other.q) > 0 else print('Res is Neg')

    def __mul__(self, other):
        return BioCells(int(self.q * other.q))

    def __truediv__(self, other):
        return BioCells(int(self.q // other.q))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.q / cells_in_row)):
            row += f'{"*" * cells_in_row}\\n'
        row += f'{"*" * (self.q % cells_in_row)}'
        return row


cells1 = BioCells(15)
cells2 = BioCells(10)
print(cells1)
print(cells2)
print(cells1 - cells2)
print(cells2 - cells1)
print(cells1 * cells2)
print(cells1 / cells2)
print(cells2.make_order(5))
print(cells1.make_order(10))
cells3 = cells1 * cells2
print(cells3.make_order(5))
