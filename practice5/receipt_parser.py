import re

text = input("Введите строку: ")

# строка с 'a' и ноль или больше 'b'
print(bool(re.search(r'ab*', text)))

# строка с 'a' и 2-3 'b'
print(bool(re.search(r'ab{2,3}', text)))

# lowercase с underscore
print(re.findall(r'[a-z]+_[a-z]+', text))

# одна заглавная + маленькие
print(re.findall(r'[A-Z][a-z]+', text))

# 'a' ... 'b'
print(bool(re.search(r'a.*b', text)))

# заменить пробел, запятую, точку на :
print(re.sub(r'[ ,.]', ':', text))

# snake -> camel
print(''.join(word.capitalize() if i > 0 else word
      for i, word in enumerate(text.split('_'))))

# split по заглавным
print(re.split(r'(?=[A-Z])', text))

# вставить пробелы перед заглавными
print(re.sub(r'(?=[A-Z])', ' ', text).strip())

# camel -> snake
print(re.sub(r'([A-Z])', r'_\1', text).lower().strip('_'))