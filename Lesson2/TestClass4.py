class Student:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'[{self.name}, {self.age}, {self.height}]'

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.age < other.age

    @staticmethod
    def print_students(students, title):
        print(title)
        for student in students:
            print(student)


if __name__ == '__main__':
    input_data = [
        ['Doron', 62, 180], ['Guy', 45, 170], ['Adi', 41, 163],
        ['Gal', 23, 171], ['Raz', 19, 173], ['Tomer', 32, 175],
    ]
    students = []
    for data in input_data:
        student = Student(data[0], data[1], data[2])
        students.append(student)
    Student.print_students(students, 'initial')

    students_sorted1 = sorted(students, key=lambda student:student.age, reverse=True)
    Student.print_students(students_sorted1, 'sorted')

    students.sort()     # in place sort
    Student.print_students(students, 'sorted in place')
