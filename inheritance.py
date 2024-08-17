class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
         return (f"{self.name} says woof!")
class Cow(Animal):
    def speak(self):
        return (f"{self.name} says mooo!")
class Sheep(Animal):
    def speak(self):
        return (f"{self.name} says meee!")
my_dog=Dog("Tommy")
my_cow=Cow("Jimmy")
my_sheep=Sheep("George")
print(my_dog.speak())
print(my_cow.speak())
print(my_sheep.speak())