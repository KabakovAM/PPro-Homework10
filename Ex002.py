class Square ():
    def __init__(self, len_a, len_b=None):
        if len_b == None:
            self.len_a = len_a
            self.len_b = len_a
        else:
            self.len_a = len_a
            self.len_b = len_b

    def square_length(self):
        print(round(2*self.len_a + 2*self.len_b, 2))

    def square_area(self):
        print(round(self.len_a*self.len_b, 2))


if __name__ == '__main__':
    a = Square(10, 5)
    a.square_length()
    a.square_area()
