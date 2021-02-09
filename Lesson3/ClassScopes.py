class Student:
    last_id = 1     # class member

    def __init__(self, name, age, height):
        # instance members
        self.id = self.get_id()
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'[{self.id}, {self.name}, {self.age}, {self.height}]'

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.age < other.age

    @classmethod
    def get_id(cls):
        id = cls.last_id
        cls.last_id += 1
        return id

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
    students = [Student(data[0], data[1], data[2]) for data in input_data]
    students_sorted = sorted(students, key=lambda student: student.age, reverse=True)
    Student.print_students(students_sorted, 'Students:')
