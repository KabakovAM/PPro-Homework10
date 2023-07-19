class Febgen():
    def __init__(self, num):
        self.num = num 

    def feb_gen(self):
        a = 0
        b = 1
        print('\n')
        print(a, end=' ')
        while self.num - 1 != 0:
            a, b = b, a + b
            print(a, end=' ')
            self.num -= 1

if __name__ == '__main__':
    a = Febgen(10)
    a.feb_gen()
    b = Febgen(20)
    b.feb_gen()