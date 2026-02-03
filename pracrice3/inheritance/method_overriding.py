class Animal:
    def sound(self):
        return "..."

class Dog(Animal):
    def sound(self):
        return "Woof!"

print(Animal().sound())
print(Dog().sound())


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 4 * 4  # допустим сторона 4

print(Shape().area())


class Person:
    def greet(self):
        return "Hello"

class Student(Person):
    def greet(self):
        return "Hello, I'm a student"

print(Person().greet())
print(Student().greet())


class Writer:
    def text(self):
        return "Base text"

class FancyWriter(Writer):
    def text(self):
        return super().text() + "!!!"

print(Writer().text())
print(FancyWriter().text())



class Book:
    def __str__(self):
        return "Just a book"

class MathBook(Book):
    def __str__(self):
        return "Math book"

print(Book())
print(MathBook())