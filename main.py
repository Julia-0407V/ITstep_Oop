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
"""
class Student:
    height = 160
    def __init__(self, height = 160):
       print( self.height)
       self.height += 10
ivan = Student()
pavlo = Student