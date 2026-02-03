words = ["aaaa", "b", "ccc", "dd"]
print(sorted(words, key=lambda s: len(s)))

nums = [-10, 3, -2, 5]
print(sorted(nums, key=lambda x: abs(x)))

pairs = [(1, 5), (2, 1), (3, 3)]
print(sorted(pairs, key=lambda t: t[1]))

names = ["Aida", "Sanzhar", "Dana"]
print(sorted(names, key=lambda s: s[-1]))

nums = [21, 14, 32, 45]
print(sorted(nums, key=lambda x: x % 10))