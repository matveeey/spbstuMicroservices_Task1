import math

class Figure:
    def __init__(self):
        self.name = ''
        self.area = 0
        self.perimeter = 0

    def __eq__(self, other):
        return self.area==other.area

    def __lt__(self, other):
        if self.area<other.area:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.area>other.area:
            return True
        else:
            return False

    def calc_area(self):
        return self.area

    def calc_perimeter(self):
        return self.perimeter
    
    def is_bigger_in_area_then(self, other):
        if (self.area > other.area):
            return True
        if (self.area < other.area):
            return False
        
    def is_equal_in_area_to(self, other):
        if (self.area == other.area):
            return True
        else:
            return False
    
    def is_bigger_in_perimeter_then(self, other):
        if (self.perimeter > other.perimeter):
            return True
        if (self.perimeter < other.perimeter):
            return False
        
    def is_equal_in_perimeter_to(self, other):
        if (self.perimeter == other.perimeter):
            return True
        else:
            return False
    
    def compare_perimeter(self, other):
        if (self.perimeter > other.perimeter):
            return f'{self.name}\'s perimeter ({self.perimeter}) is higher than {other.name}\'s ({other.perimeter})'
        if (self.perimeter < other.perimeter):
            return f'{self.name}\'s perimeter ({self.perimeter}) is smaller than {other.name}\'s ({other.perimeter})'
        if (self.perimeter == other.perimeter):
            return f'{self.name}\'s perimeter ({self.perimeter}) is equal to {other.name}\'s ({other.perimeter})'

# Rectangle
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

        self.name = 'Rectangle'
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_area(self):
        return self.a * self.b
    
    def calc_perimeter(self):
        return 2 * (self.a + self.b)

# Triangle
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

        self.name = 'Triangle'
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    @classmethod
    def equilateral(cls, a):
        return cls(a, a, a)

    def calc_area(self):
        return math.sqrt(self.perimeter) * (self.perimeter - self.a) * (self.perimeter - self.b) * (self.perimeter - self.c)
    
    def calc_perimeter(self):
        return self.a + self.b + self.c

# Circle
class Circle(Figure):
    def __init__(self, r):
        self.r = r

        self.name = 'Circle'
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_area(self):
        return math.pi * math.pow(self.r, 2)
    
    def calc_perimeter(self):
        return 2 * math.pi * self.r

# Square
class Square(Rectangle):
    def __init__(self, a):
        self.a = a
        self.b = a

        self.name = 'Square'
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

def compare_area(fig_0: Figure, fig_1: Figure):
    result = ''
    if (fig_0.is_equal_in_area_to(fig_1)):
        result = 'is equal to'
    else:
        if (fig_0.is_bigger_in_area_then(fig_1)):
            result = 'bigger than'
        else:
            result = 'smaller than'
    print (f'Figure {fig_0.name} of area {fig_0.area} {result} than {fig_1.name} of area {fig_1.area}')

def compare_perimeter(fig_0: Figure, fig_1: Figure):
    result = ''
    if (fig_0.is_equal_in_perimeter_to(fig_1)):
        result = 'is equal to'
    else:
        if (fig_0.is_bigger_in_perimeter_then(fig_1)):
            result = 'bigger than'
        else:
            result = 'smaller than'
    print (f'Figure {fig_0.name} of perimeter {fig_0.perimeter} {result} than {fig_1.name} of perimeter {fig_1.perimeter}')

if __name__ == '__main__':
    # squares
    square_a = Square(10)
    square_b = Square(9)

    # rectangles
    rectangle_a = Rectangle(8, 10)
    rectangle_b = Rectangle(20, 1)

    # triangles
    triangle_a = Triangle(1, 2, 3)
    triangle_b = Triangle.equilateral(2)

    # circles
    circle_a = Circle(2)
    circle_b = Circle(4)

    print('')
    compare_area(rectangle_a, triangle_b)
    compare_area(triangle_a, circle_b)
    compare_area(triangle_b, square_a)
    compare_area(square_b, rectangle_b)
    compare_area(triangle_b, triangle_b)

    print('')
    compare_perimeter(rectangle_a, triangle_b)
    compare_perimeter(triangle_a, circle_b)
    compare_perimeter(triangle_b, square_a)
    compare_perimeter(square_b, rectangle_b)
    compare_perimeter(triangle_b, triangle_b)

    print('')
    # overloaded compare operators
    if (circle_a < square_b):
        print (f'{circle_a.name} has smaller area than {square_b.name}')

    print('')