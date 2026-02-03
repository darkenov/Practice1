class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

x = Student("Mike", "Olsen")
x.printname()

class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    pass

d = Dog()
print(d.sound())  # "..."


class Animal:
    def sound(self):
        return "..."

class Cat(Animal):
    def meow(self):
        return "Meow"

c = Cat()
print(c.sound())  # "..."
print(c.meow())   # "Meow"


class Animal:
    def sound(self):
        return "..."

class Cow(Animal):
    def sound(self):
        return "Moo"

a = Animal()
cow = Cow()
print(a.sound())    # "..."
print(cow.sound())  # "Moo"