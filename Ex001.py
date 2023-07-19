from math import pi


class Circle ():
    def __init__(self, radius):
        self.radius = radius

    def circle_length(self):
        print(round(2*pi*self.radius, 2))

    def circle_area(self):
        print(round(pi*self.radius**2, 2))


if __name__ == '__main__':
    a = Circle(10)
    a.circle_length()
    a.circle_area()
