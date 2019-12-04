import datetime
class Car:

    def __init__(self, year_or_production, color):
        self.year = year_or_production
        self.color = color

    def calculate_age(self, current_year):
        return current_year - self.year

    def change_color(self, color):
        self.color = color

a = int(input('Age'))
b = str(input('color'))
c = Car(a, b)
print(c.year)
age = c.calculate_age(2019)
c.change_color('white')
print(age)
print(c.color)