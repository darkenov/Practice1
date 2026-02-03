class Phone:
    code = "+7"

print(Phone.code)

class Bank:
    limit = 1000

print(Bank.limit)

class Counter:
    value = 0

Counter.value += 1
Counter.value += 1
print(Counter.value)  # 2

class App:
    version = 1

print(App.version)
App.version = 2
print(App.version)

class Group:
    names = []

Group.names.append("Aida")
Group.names.append("Sanzhar")
print(Group.names)