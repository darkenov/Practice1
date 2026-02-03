nums = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, nums)))

nums = [-3, 0, 4, -1, 7]
print(list(filter(lambda x: x > 0, nums)))

words = ["a", "ab", "abc", "hello"]
print(list(filter(lambda s: len(s) >= 3, words)))

nums = [5, 10, 12, 15, 22]
print(list(filter(lambda x: x % 5 == 0, nums)))

words = ["apple", "banana", "avocado", "pear"]
print(list(filter(lambda s: s[0] == "a", words)))