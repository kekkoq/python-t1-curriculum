import random

fruits = ["apple", "orange", "grapes", "banana"]

for i in range(5):
    print(fruits[random.randint(0, len(fruits) - 1)])