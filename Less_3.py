class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
    def add_passengers (self, *args):
        for passengers in args:
            self.passengers.append(passengers)
    def print_passengers_name (self):
        if self.passengers !=[]:
           print(f"Імена пасажирів")
           for passengers in self.passengers:
               print (passengers.name)

        else: print (f"Немає пасажирів в автомобілі {self.brand}")

Kiril = Human("Kiril")
Igor = Human("Igor")
car = Auto("Mercedes")
car.add_passengers(Kiril, Igor )
car.print_passengers_name()




