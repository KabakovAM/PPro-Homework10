class Animal ():
    def __init__(self, name, age, prop):
        self.name = name
        self.age = age
        self.prop = prop

    def print_info(self):
        print(self.prop)


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.prop = breed


class Fish(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
        self.prop = color


class Bird(Animal):
    def __init__(self, name, age, speed):
        super().__init__(name, age, speed)
        self.prop = speed


class Elifant(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.prop = weight


if __name__ == '__main__':
    a = Dog('Фёдор', 5, 'Овчарка')
    b = Fish('Петя', 2, 'Золотая')
    c = Bird('Ольга', 6, 25)
    d = Elifant('Генадий', 15, 1200)
    a.print_info()
    b.print_info()
    c.print_info()
    d.print_info()