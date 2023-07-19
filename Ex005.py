class Dog():
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def print_info(self):
        print(self.breed)


class Fish():
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def print_info(self):
        print(self.color)


class Bird():
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def print_info(self):
        print(self.speed)


class Elifant():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.weight)


if __name__ == '__main__':
    a = Dog('Фёдор', 5, 'Овчарка')
    b = Fish('Петя', 2, 'Золотая')
    c = Bird('Ольга', 6, 25)
    d = Elifant('Генадий', 15, 1200)
    a.print_info()
    b.print_info()
    c.print_info()
    d.print_info()
