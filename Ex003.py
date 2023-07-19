class Man ():
    def __init__(self, fcs, age, country):
            self.fcs = fcs
            self.__age = age
            self.country = country

    def change_age(self):
         self.__age += 1

    def fcs_print(self):
        print(self.fcs)

    def age_print(self):
        print(self.__age)

    def country_print(self):
        print(self.country)


if __name__ == '__main__':
    a = Man('Иванов Иван Иванович', 41, 'Россия')
    a.fcs_print()
    a.age_print()
    a.change_age()
    a.age_print()
    a.country_print()