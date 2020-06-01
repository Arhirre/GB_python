# _author_ = Nikita_Savchenko


class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def coat_material(self):
        return self.size / 6.5 + 0.5

    def jaket_material(self):
        return self.height * 2 + 0.3

    def coat_jaket_material(self):
        return (self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)

    @property
    def total_mat_prop(self):
        return str(f'{(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)} total mats')


measurements = Clothes(50, 1.82)
print(measurements.coat_material())
print(measurements.jaket_material())
print(measurements.coat_jaket_material())


class AbsCoat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.material_c = self.size / 6.5 + 0.5

    def __str__(self):
        return f'{self.material_c} for Coat'


class AbsJacket(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.material_j = self.height * 2 + 0.3

    def __str__(self):
        return f'{self.material_j} for Jacket'


coat = AbsCoat(50, 1.82)
print(coat)
jacket = AbsJacket(50, 1.82)
print(jacket)
print(coat.total_mat_prop)
print(coat.coat_material())
