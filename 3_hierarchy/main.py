import math

class figure:
    def __init__(self):
        self.name = ''
        self.area = 0
        self.perimeter = 0

    def __eq__(self, other):
        if self.area==other.area:
            return True
        else:
            return False

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
    
    def compare_area(self, other):
        if (self.area > other.area):
            return f'{self.name}\'s area ({self.area}) is higher than {other.name}\'s ({other.area})'
        if (self.area < other.area):
            return f'{self.name}\'s area ({self.area}) is smaller than {other.name}\'s ({other.area})'
        if (self.area == other.area):
            return f'{self.name}\'s area ({self.area}) is equal to {other.name}\'s ({other.area})'
    
    def compare_perimeter(self, other):
        if (self.perimeter > other.perimeter):
            return f'{self.name}\'s perimeter ({self.perimeter}) is higher than {other.name}\'s ({other.perimeter})'
        if (self.perimeter < other.perimeter):
            return f'{self.name}\'s perimeter ({self.perimeter}) is smaller than {other.name}\'s ({other.perimeter})'
        if (self.perimeter == other.perimeter):
            return f'{self.name}\'s perimeter ({self.perimeter}) is equal to {other.name}\'s ({other.perimeter})'

# rectangle
class rectangle(figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

        self.name = 'rectangle'
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_area(self):
        return self.a * self.b
    
    def calc_perimeter(self):
        return 2 * (self.a + self.b)

# triangle
class triangle(figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

        self.name = 'triangle'
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    @classmethod
    def equilateral(cls, a):
        return cls(a, a, a)

    def calc_area(self):
        return math.sqrt(self.perimeter) * (self.perimeter - self.a) * (self.perimeter - self.b) * (self.perimeter - self.c)
    
    def calc_perimeter(self):
        return self.a + self.b + self.c

# circle
class circle(figure):
    def __init__(self, r):
        self.r = r

        self.name = 'circle'
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_area(self):
        return math.pi * math.pow(self.r, 2)
    
    def calc_perimeter(self):
        return 2 * math.pi * self.r

# square
class square(rectangle):
    def __init__(self, a):
        self.a = a
        self.b = a

        self.name = 'square'
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

if __name__ == '__main__':
    # squares
    square_a = square(10)
    square_b = square(9)

    # rectangles
    rectangle_a = rectangle(8, 10)
    rectangle_b = rectangle(20, 1)

    # triangles
    triangle_a = triangle(1, 2, 3)
    triangle_b = triangle.equilateral(2)

    # circles
    circle_a = circle(2)
    circle_b = circle(4)

    print(rectangle_a.compare_area(triangle_b))
    print(triangle_a.compare_area(circle_b))
    print(triangle_b.compare_area(square_a))
    print(square_b.compare_area(rectangle_b))

    # overloaded compare operators
    if (circle_a < square_b):
        print (f'{circle_a.name} has smaller area than {square_b.name}')