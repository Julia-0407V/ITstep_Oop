"""
class Student:
    print("Hi")
    def __init__(self):
        self.height = 160
        print ("I'm alive!")

ivan = Student:
"""
"""
class Student:
    amount = 0
    def __init__(self, height = 160):
        self.height = height
        Student.amount += 1
ivan = Student()
pavlo = Student(height = 170)
print(ivan.amount)
print(Student.amount)

class Student:
    height = 160
    def __init__(self, height = 160):
       print( self.height)
       self.height += 10
ivan = Student()
pavlo = Student()
"""
"""
class Student:
    def __init__(self, name  = None, height = 160):
         self.name = name
         self.height = height
    def __bool__(self):
        return self.name != None
    def __len__(self):
        return self.height
    def __del__(self):
        print("Training is over")

ivan = Student()
print(ivan.__len__())
print(ivan.__bool__())
print(len(ivan))
print(bool(ivan))
"""
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        return f"Ім'я:{self.name}, Вік:{self.age}"

student1=Student("Кіріл", 15)
print(student1.get_info())
"""
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius**2
circle1=Circle(5)
print(circle1.area())
"""

import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to study ")
        self.gladness += 0.12
        self.progress -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time ")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if  self.progress <= -0.5:
            print("Cast out...")
            self.alive = False
        elif  self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress >= 5:
            print("Excellent!!!")
            self.alive = False


    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = { self.progress, 2}")

    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"day = {day:=^50}")

        live_cube = random.randint(1,3)
        if  live_cube == 1:
            self.to_study()
        elif  live_cube == 2:
            self.to_sleep()
        elif  live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()
pasha = Student(name = "Pasha")
for day in range(365):
    if pasha.alive == False:
        break
pasha.live(day)