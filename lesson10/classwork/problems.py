import random

# Problem 1  ( 1 : 1 )
# Create a variable for your favorite hobby and print it.
hobby = "Sleeping"
print(hobby)

# Problem 2  ( 1 : 1 )
# Ask the user for a number.
# Print the number multiplied by 3.
asked_number = int(input("Enter a number: "))
print(asked_number * 3)


# Problem 3  ( 1 : 1 )
# Print every number from 5 to 10 (inclusive) using a for loop.
num = 5
while num<= 10:
    print(num)
    num += 1


# Problem 4  ( 2 : 1 )
# Ask the user for two numbers. 
# Print whether the first is larger, smaller, or equal to the second.
# Ask the user for two numbers
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
if first > second:
    print("The first number is larger.")
elif first < second:
    print("The first number is smaller.")
else:
    print("The numbers are equal.")


# Problem 5  ( 2 : 1 )
# Use the modulo operator to print whether a random number from 1 to 20 is divisible by 4.
num = random.randint(1, 20)
print("Random number:", num)
if num % 4 == 0:
    print("It is divisible by 4.")
else:
    print("It is not divisible by 4.")



# Problem 6  ( 2 : 1 )
# Ask the user for a number between 1 and 10.
# Use logical operators to print whether it’s in the lower half (1–5), upper half (6–10) or out of range.
num = int(input("Enter a number within 1 and 10: "))
if num <5:
    print("Your number is in the lower half")
elif num >= 6 and num <= 10:
    print("Your number is in the upper half")
else:
    print("Your number is out of range")


# Problem 7  ( 2 : 1 )
# Create a list of 5 animals. 
# Print the length of the list and the second animal.
animals = ["Penguin", "Tiger", "Squid", "Wolf", "Eagle"]
print("Length of list:", len(animals))
print("Second animal:", animals[1])


# Problem 8  ( 3 : 1 )
# Get a random item from the list of colors and print it.
colors = ["red", "blue", "green", "yellow"]
chosen_color = random.choice(colors)
print("Random color:", chosen_color)



# Problem 9  ( 3 : 2 )
# Ask the user for a number.
# Use a for loop to count how many items in the list of numbers are greater than the user’s number.
# Ask the user for a number
asked_number2 = int(input("Enter a random number: "))
numbers = [3, 8, 15, 2, 9, 12]
count = 0
for num in numbers:
    if num > asked_number2:
        count += 1

# Print the result
print("There are", count, "numbers greater than", asked_number2)

# Problem 10  ( 3 : 2 )
# Find the largest number in the list and print it.
numbers = [14, 27, 5, 89, 42]
print("The biggest number is:", max(numbers))



# Problem 11  ( 4 : 2 )
# Write a function that takes two numbers and returns their sum.
# Ask the user for two numbers and use your function to print the result.
# Define a function that returns the sum of two numbers

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
print((first + second))

# Problem 12  ( 4 : 2 )
# Create a global counter starting at 0.
# Write a function that increases it by a random number from 1–5 and prints it.
counter = 0

def increase_counter():
    global counter
    counter += random.randint(1, 5)
    print("Counter is now:", counter)
increase_counter()



# Problem 13  ( 5 : 3 )
# Ask the user for a starting number less than 50.
# Use a while loop to add 7 each time until the number is >= 50.
# Print the number at each iteration of the loop.
asked_number3 = int(input("Enter a number that is under 50: "))
while asked_number3 <= 50:
    asked_number3 += 7
    print(asked_number3)

# Problem 14  ( 6 : 3 )
# Create a list of 6 random integers between 1 and 100.
# Print the list, the sum of its numbers, and how many are even.
random_numbers = [7, 25, 56, 64, 77, 80]


# Problem 15  ( 7 : 3 )
# Ask the user for 4 words. Store them in a list.
# While the list is not empty:
# - Remove and print the first word.
# - Then print how many words are left.
print("\n")
word = []
for n in range(4):
    word.append(input("Enter a word: "))
while len(words)>0:
    print("Removed", words.pop(0))
    print("words left:", len(words))