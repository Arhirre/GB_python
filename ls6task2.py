# _author_ = Nikita_Savchenko


class Road:
    __weight_per_meter = 25
    __road_thicc = 5

    def __init__(self, Length, width):
        self._length = Length
        self._width = width

    def mass(self):
        mass = self._length * self._width * self.__weight_per_meter * self.__road_thicc / 1000
        print(f'You need {mass} - tons of asphalt.')


road_builder = Road(int(input('Enter road length in meters: ')), int(input('Enter road width in meters: ')))
road_builder.mass()
