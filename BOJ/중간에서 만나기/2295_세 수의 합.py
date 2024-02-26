from itertools import product

numbers = set()

numbers_count = int(input())

for _ in range(numbers_count):
    numbers.add(int(input()))

sample = set()

for number1, number2 in product(numbers,repeat=2):
    sample.add(number1+ number2)

temp = -1
for number1, number2 in product(numbers,repeat=2):
    number1, number2 = min(number1, number2), max(number1, number2)
    if (number2 - number1) in sample:
        temp = max(temp, number2)

print(temp)