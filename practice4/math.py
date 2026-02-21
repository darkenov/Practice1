#1) Градусы в радианы
deg = float(input())
rad = deg * 3.141592653589793 / 180
print(rad)
#2) Площадь трапеции

Формула: S = (a + b) / 2 * h

h = float(input())
a = float(input())
b = float(input())

area = (a + b) / 2 * h
print(area)
#3) Площадь правильного многоугольника

Формула: S = (n * a^2) / (4 * tan(pi/n))

import math

n = int(input())
a = float(input())

area = (n * a * a) / (4 * math.tan(math.pi / n))
print(area)
#4) Площадь параллелограмма

Формула: S = base * height

base = float(input())
h = float(input())

print(base * h)