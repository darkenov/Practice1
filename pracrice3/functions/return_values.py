def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

def get_greeting():
  return "Hello from a function"

print(get_greeting())

def double(x):
    return x * 2

print(double(7))

def is_even(n):
    return n % 2 == 0

print(is_even(10))  
print(is_even(7))