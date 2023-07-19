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


class Employee(Man):
    def __init__(self, fcs, age, country, employee_id):
        super().__init__(fcs, age, country)
        self.employee_id = employee_id
        self.level = sum(int(i) for i in str(employee_id)) / 7

    def employee_id_print(self):
        print(self.employee_id)

    def level_print(self):
        print(self.level)


if __name__ == '__main__':
    a = Employee('Иванов Иван Иванович', 41, 'Россия', 365421)
    a.fcs_print()
    a.age_print()
    a.change_age()
    a.age_print()
    a.country_print()
    a.employee_id_print()
    a.level_print()
