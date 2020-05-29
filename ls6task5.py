# _author_ = Nikita_Savchenko


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Enabling Drawing!'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took a {self.title}. Lets wright some lines!'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took a {self.title}. Lets make a sketch!'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'You took a {self.title}. Lets add some color!'


draw = Stationery('Tool')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

print(draw.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
