class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def area(self):
        return self.a*self.b

    @classmethod
    def calculate_area(cls, a, b):
        cls.__init__(cls, a, b)
        return cls.a*cls.b

    def __str__(self):
        return f'a={self.a} b={self.b} area={self.a*self.b}'

   
print(Rectangle(2,3))
print(Rectangle.calculate_area(2,3))
