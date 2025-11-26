import random
fruits = ["apple", "banana", "orange"]

fruits.append("kiwi")
print(fruits)

fruits.insert(1, "grapes")
print(fruits[2])
print(fruits)
fruits.insert(1, "kiwi")
fruits.remove("kiwi")
fruits.remove("kiwi")
print(fruits)
for i in fruits:
    if (i == "kiwi"):
        fruits.remove("kiwi")
print(fruits)

x = fruits.pop()
print(x)

y = fruits.pop(0)
print(fruits)
print(y)

length = len(fruits)
random_index = random.randint(0, length - 1)
c = fruits[random.index]
print(c)