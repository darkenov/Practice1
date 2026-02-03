class Runner:
    def run(self):
        return "Running"

class Swimmer:
    def swim(self):
        return "Swimming"

class Triathlete(Runner, Swimmer):
    pass

t = Triathlete()
print(t.run())
print(t.swim())



class A:
    def who(self):
        return "A"

class B:
    def who(self):
        return "B"

class C(A, B):
    pass

print(C().who())  # будет "A", потому что A стоит первым



class A:
    def who(self):
        return "A"

class B:
    def who(self):
        return "B"

class C(B, A):
    pass

print(C().who())  # теперь "B"



class Base:
    def hello(self):
        return "Base"

class Left(Base):
    def hello(self):
        return "Left -> " + super().hello()

class Right(Base):
    def hello(self):
        return "Right -> " + super().hello()

class Child(Left, Right):
    def hello(self):
        return "Child -> " + super().hello()

print(Child().hello())
# MRO: Child -> Left -> Right -> Base



class Printable:
    def show(self):
        return "Showing"

class Saveable:
    def save(self):
        return "Saving"

class Document(Printable, Saveable):
    pass

d = Document()
print(d.show())
print(d.save())