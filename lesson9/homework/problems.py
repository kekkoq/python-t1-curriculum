# Problem 1
# Use a while loop to print the word "Python" 4 times.

count = 0
while count < 4:
    print("Python")
    count += 1


# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).num = 2
num = 2
while num<= 12:
    print(num)
    num += 2

# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.
# Ask the user for a positive number
limit = int(input("Enter a positive number: "))
count = 0
while count <= limit:
    print(count)
    count += 1

# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.
start = int(input("Enter a starting number greater than 10: "))
while start >= 0:
    print(start)
    start -= 5

# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
# Create a list of your three favorite animals
animals = ["Penguin", "Tiger", "Squid"]
index = 0
while index < len(animals):
    print(animals[index] + " is awesome!")
    index += 1

