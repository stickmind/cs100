import operator
from urllib.request import urlopen

# self-evaluating primitives
print(29)
print("this is a string")
print(True)

# combination
print(2 + 3)
print((2 * 3) + 4)

# using names to abstract an expression
score = 23
total = operator.add(12, 13)
print(100 * (score / total))

# more complex expression
print("Wait a minute...")
shakespeare = urlopen('https://www.composingprograms.com/shakespeare.txt')
words = set(shakespeare.read().decode().split())
print({w for w in words if len(w) == 6 and w[::-1] in words})
