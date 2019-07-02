'''
from math import pi
class Circle:

    def __init__(self, r):
        self.r = r
        
    def area(self):
        self.area = pi*self.r**2

    def perimeter(self):
        self.perimeter = pi*self.r*2

    def __str__(self):
        self.area()
        self.perimeter()
        return f'r={self.r} area={round(self.area, 2)} perimeter={round(self.perimeter, 2)}'


print(Circle(3))
'''   


from math import pi
class Circle:

    def __init__(self, r):
        self.r = r
        
    def area(self):
        return pi*self.r**2

    def perimeter(self):
        return pi*self.r*2

    def __str__(self):
        return f'r={self.r} area={round(self.area(), 2)} perimeter={round(self.perimeter(), 2)}'


print(Circle(3))
   

