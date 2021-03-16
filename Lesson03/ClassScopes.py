class Student:
    last_id = 1     # class member

    def __init__(self, name, age, height):
        # instance members
        self.id, Student.last_id = Student.last_id, Student.last_id+1
        # Note: The next line will not work
        #  it will create instance member that will hide class member and +1 it
        #  Student.last_id will not be incremented
        # self.id, self.last_id = self.last_id, self.last_id + 1
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return f'[{self.id}, {self.name}, {self.age}, {self.height}]'

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    student1 = Student('Doron', 62, 180)
    print(f'student {student1}, Sudent.last_id:{Student.last_id}')
