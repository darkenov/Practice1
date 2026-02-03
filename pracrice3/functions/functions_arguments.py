def addition(a,b):
    print(a+b)
addition(4,5)

def greet(name):
    print("Hello,", name)

greet("Aida")

def power(x, p=2):
    return x ** p

print(power(4))    
print(power(4, 3))

def min_max(a, b):
    if a < b:
        return a, b
    else:
        return b, a

mn, mx = min_max(10, 7)
print(mn, mx)

def mult(a, b):
    return a * b

print(mult(3, 5))