#1) Квадраты чисел до N
def squares_to_n(n):
    for i in range(n + 1):
        yield i * i

n = int(input())
for x in squares_to_n(n):
    print(x)
#2) Чётные числа от 0 до n (через запятую)
def evens(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
print(",".join(str(x) for x in evens(n)))
#3) Числа кратные 3 и 4 (то есть 12) от 0 до n
def mult_12(n):
    for i in range(0, n + 1):
        if i % 12 == 0:
            yield i

n = int(input())
for x in mult_12(n):
    print(x, end=" ")
#4) Квадраты от a до b
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

a, b = map(int, input().split())
for x in squares(a, b):
    print(x)
#5) Все числа от n до 0
def down(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for x in down(n):
    print(x)