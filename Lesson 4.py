class Human:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, model):
        self.model = model
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f"{passenger.name} сів у авто")

    def info(self):
        print(f"Авто, модель - {self.model}")
        if self.passengers != []:
            print("Зараз в автівці їдуть:")
            for passanger in self.passengers:
                print(passanger.name)


car = Car("Tesla Molel M")
car.info()
human1 = Human("Vasya")
human2 = Human("Kolya")
car.add_passenger(human1)
car.add_passenger(human2)
car.info()

