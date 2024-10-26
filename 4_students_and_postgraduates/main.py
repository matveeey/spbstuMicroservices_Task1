import math

# student
class student:
    def __init__(self, name, age, group_number):
        self.name = name
        self.age = age
        self.group_number = group_number
        self.scholarship = 0
        self.scholarship_levels = { 5: 6000, 4: 4000 }
        self.marks = []

    def append_mark(self, mark):
        self.marks.append(mark)
        self.__calc_scholarship()

    def info(self):
        print(f'')
        print(f'student {self.name}')
        print(f'age {self.age}')
        print(f'scholarship {self.scholarship}')

    def compare_scholarship(self, other):
        if (self.scholarship > other.scholarship):
            print(f'{self.name}\'s scholarship ({self.scholarship}) is higher than {other.name}\'s one ({other.scholarship})')
        if (self.scholarship < other.scholarship):
            print(f'{self.name}\'s scholarship ({self.scholarship}) is less than {other.name}\'s one ({other.scholarship})')
        if (self.scholarship == other.scholarship):
            print(f'{self.name}\'s scholarship ({self.scholarship}) and {other.name}\'s one ({other.scholarship}) are equal')

    def __calc_scholarship(self):
        if (len(self.marks) == 0):
            return
        avg = 0
        for mark in self.marks:
            avg += mark
        avg /= len(self.marks)
        
        calcd_scholarship = self.scholarship_levels.get(int(avg))
        if calcd_scholarship == None:
            return
        self.scholarship = calcd_scholarship

# postgraduate
class postgraduate(student):
    def __init__(self, name, age, group_number, study):
        super().__init__(name, age, group_number)
        self.scholarship_levels = { 5: 8000, 4: 6000 }
        self.study = study
    
    def info(self):
        super().info()
        print(f'graduate work: {self.study}')

if __name__ == '__main__':
    student_a = student('Igor', 11, 1337)

    student_a.append_mark(5)
    student_a.info()

    student_a.append_mark(5)
    student_a.append_mark(1)
    student_a.info()

    student_a.append_mark(5)
    student_a.append_mark(5)
    student_a.append_mark(5)
    student_a.append_mark(5)
    student_a.info()

    postgraduate_a = postgraduate('Ivan', 28, 228, 'Aerial vehicles and animals in the forests')
    postgraduate_a.append_mark(3)
    postgraduate_a.info()

    postgraduate_a.compare_scholarship(student_a)

    postgraduate_a.append_mark(5)
    postgraduate_a.append_mark(5)
    postgraduate_a.append_mark(5)
    postgraduate_a.append_mark(5)
    postgraduate_a.compare_scholarship(student_a)
