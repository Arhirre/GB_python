# _author_ = Nikita_Savchenko


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} - started moving!'

    def stop(self):
        return f'{self.name} - Stopped!'

    def turn_left(self):
        return f'{self.name} - Turned Left!'

    def turn_right(self):
        return f'{self.name} - Turned Right!'

    def show_speed(self):
        return f'Speed of {self.name} = {self.speed}!'

    def police(self):
        return f'{self.name} is not a police car!'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Speed of T.car {self.name} is {self.speed}! Warning - OVER SPEED!'
        else:
            return f'Speed of T.car {self.name} is {self.speed}.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Speed of W.car {self.name} is {self.speed}! Warning - OVER SPEED!'
        else:
            return f'Speed of W.car {self.name} is {self.speed}.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'This {self.name} is police car!'


nissan = TownCar(45, 'Silver', 'Nissan', False)
ferrari = SportCar(300, 'Red', 'Ferrari', False)
mercedes = WorkCar(60, 'Black', 'Mercedes', False)
ford = PoliceCar(120, 'Blue', 'Ford', True)

print(f'{ford.go()}, and {nissan.stop()}')
print(f'{ferrari.show_speed()}, and its color is {ferrari.color}')
print(f'{ford.police()}, and {mercedes.police()}')
