class Student:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'[{self.name}, {self.age}, {self.height}]'

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    input_data = [
        ['Doron', 62, 180], ['Guy', 45, 170], ['Adi', 41, 163],
        ['Gal', 23, 171], ['Raz', 19, 173], ['Tomer', 32, 175],
    ]
    students = [Student(data[0], data[1], data[2]) for data in input_data]
    print(students)


