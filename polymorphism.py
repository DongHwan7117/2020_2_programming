class Person:
    def __init__(self, name):
        self.name = name

    def work(self):
        print (self.name + " works hard")        

class physicist(Person):
    def work(self):
        print (self.name + " do well in definition")

class mathematician(Person):
    def work(self):
        print (self.name + " do well in intuition")



person1 = physicist("Dave")
person2 = mathematician("David")
person1.work()
person2.work()