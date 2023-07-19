class Animal ():
    def __init__(self, name, age, prop):
        self.name = name
        self.age = age
        self.prop = prop

    def print_info(self):
        print(self.prop)


class Factory(Animal):
    def __init__(self, animal, name, age, prop):
        self.animal = animal
        super().__init__(name, age, prop)

    def create_animal(self):
        if self.animal == 'Dog':
            return Dog(self.name, self.age, self.prop)
        elif self.animal == 'Fish':
            return Fish(self.name, self.age, self.prop)
        elif self.animal == 'Bird':
            return Bird(self.name, self.age, self.prop)
        elif self.animal == 'Elifant':
            return Elifant(self.name, self.age, self.prop)


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
    a = Factory('Dog', 'Фёдор', 5, 'Овчарка')
    a.create_animal()
    b = Factory('Fish', 'Петя', 2, 'Золотая')
    b.create_animal()
    c = Factory('Bird', 'Ольга', 6, 25)
    c.create_animal()
    d = Factory('Elifant', 'Генадий', 15, 1200)
    d.create_animal()
    a.print_info()
    b.print_info()
    c.print_info()
    d.print_info()
