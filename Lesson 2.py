
class Student:
    print("Hi")
    count_of_student = 0
    def __init__(self, name, height = 160):
        self.height = height
        self.name = name
        Student.count_of_student += 1
        print("Hi! I`m Student")

    def grow_up(self, grow=1):
        if self.height + grow < 220:
            self.height += grow

    def info(self):
        print(f"Name   : {self.name}")
        print(f"Height : {self.height}")

    def __str__(self):
        return f"Name   : {self.name}\nHeight : {self.height}"

    def __del__(self):
        Student.count_of_student -= 1
        print(f"{self.name} is dead :(")

    def __len__(self):
        return self.height

print(Student.count_of_student)

student1 = Student("Serg")
# print(student1.name)
student1.grow_up(15)
# print(student1.height)
# student1.info()

print(student1)

print(Student.count_of_student)

student2 = Student("Vasya", 190)
# student2.height = 17000000000000
# print(student2.name)
# print(student2.height)
# student2.info()
print(student2)
print(Student.count_of_student)

print(len(student2))