# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
a_number = 9
if a_number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
day_of_the_week = "Tuesday"

if day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    print("Weekend")
else:
    print("Weekday")
# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
import random
for i in range(1):
    num = random.randint(1, 10)
    print(num)
if num == 5:
    print("Correct!")
else:
    print("Try again!")
# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
positive_interger = 721
if positive_interger % 2 == 0 and positive_interger > 10:
    print("Big even number")
else:
    print("Number does not meet criteria")



# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".
number_1 = 5412
number_2 = 217
if number_1 == number_2:
    print("Numbers are equal")

