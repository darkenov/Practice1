fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

a=12
for i in range(1,a):
    if i%3==0:
        break
    print(i)

mystr = "banana"
for x in range(len(mystr)):
    if "n" in mystr[x]:
        break
    print(mystr[x])

b=15
for i in range(1,b):
    if i%5==0:
        break
    print(i)


