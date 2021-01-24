class Student:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


if __name__ == '__main__':
    input_data = [
        ['Doron', 62, 180], ['Guy', 45, 170], ['Adi', 41, 163],
        ['Gal', 23, 171], ['Raz', 19, 173], ['Tomer', 32, 175],
    ]
    students = []
    for data in input_data:
        student = Student(data[0], data[1], data[2])
        students.append(student)
    print(students)


