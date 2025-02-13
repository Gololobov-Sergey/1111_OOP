
class Human:
    height = 170
    progress = 10

    def info(self):
        print(f"Height   - {self.height}")
        print(f"Progress - {self.progress}")

class Student(Human):
    progress = 20

class Worker(Human):
    salary = 1000


human = Human()
#print(human.height)
human.info()
print()

student = Student()
# print(student.height)
# print(student.progress)
student.info()

worker = Worker()
# print(worker.height)
# print(worker.salary)


class A:
    a = 10

class B(A):
    #a = 20
    b = 30

class C(B):
    c = 40
    def __init__(self):
        print(self.a)
        print(self.b)
        print(self.c)

#c = C()

class Test:
    def __init__(self):
        self.test1 = 100
        self._test2 = 200
        self.__test3 = 300

    def hello(self):
        print("Hello")
        self.__hello()

    def _hello(self):
        print("_Hello")

    def __hello(self):
        print("__Hello")

    def setTest(self, t):
        if t < 100:
            self.__test3 = t

    def getTest(self):
        return self.__test3


class Test2(Test):
    def info(self):
        print(self.test1)
        print(self._test2)
        print(self.__test3)


# test = Test()
# test.hello()
# test._hello()
# #test.__hello()
#
# t2 = Test2()
# t2.info()

class Hello:
    def __init__(self):
        self.hello = "Hello"

    def info(self):
        print("Hello")

class World(Hello):
    def __init__(self):
        super().__init__()
        self.world = "World"

    def info(self):
        super().info()
        print("World")


hw = World()

print(hw.hello + " " + hw.world)
hw.info()