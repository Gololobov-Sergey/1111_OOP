import random


class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 10
        self.gladness = 50
        self.alive = True

    def study(self):
        self.progress += 1
        self.gladness -= 1
        print("Я навчаюсь у IT STEP")


    def chill(self):
        self.gladness += 1
        self.progress -= 1
        print("Я сьогодні гарно відпочив :)")


    def sleep(self):
        self.gladness += 0.5
        print("Я втомився, і пішов спати ...")


    def is_alive(self):
        if self.gladness < 0:
            print("В мене дипресія, я пішов ...")
            self.alive = False
        elif self.progress < 0:
            print("Нічого не лізе в голову.... Кінець")
            self.alive = False
        elif self.progress > 50:
            print("Я достроково завершив IT STEP, і пішов працювати")
            self.alive = False

    def info(self):
        print(f"Задоволення - {self.gladness}")
        print(f"Прогрес     - {self.progress}")


    def live(self, day):
        print()
        print(f"  ----- День №{day+1} -----")
        print(f"Привіт, я {self.name}. І я сьогодні:")
        rnd = random.randint(1,3)
        if rnd == 1:
            self.study()
        elif rnd == 2:
            self.sleep()
        elif rnd == 3:
            self.chill()

        self.info()
        self.is_alive()



student = Student("Vasya")
for day in range(365):
    if student.alive == False:
        break
    student.live(day)


