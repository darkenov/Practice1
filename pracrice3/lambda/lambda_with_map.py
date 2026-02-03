nums = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, nums)))

nums = [5, 0, -2]
print(list(map(lambda x: x + 10, nums)))

nums = [7, 8, 9]
print(list(map(lambda x: str(x), nums)))


words = ["ab", "hello", "x"]
print(list(map(lambda s: len(s), words)))

nums = [2, 3, 4]
print(list(map(lambda x: x ** 2, nums)))