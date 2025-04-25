import random
import math

class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius

length = random.uniform(1.0, 10.0)
width = random.uniform(1.0, 10.0)
rect = Rectangle(length, width)
print(f"Прямокутник: довжина = {length:.2f}, ширина = {width:.2f}")
print(f"Площа прямокутника: {rect.get_area():.2f}")
print(f"Периметр прямокутника: {rect.get_perimeter():.2f}")
print()
radius = random.uniform(1.0, 10.0)
circle = Circle(radius)
print(f"Коло: радіус = {radius:.2f}")
print(f"Площа кола: {circle.get_area():.2f}")
print(f"Довжина кола: {circle.get_circumference():.2f}")
