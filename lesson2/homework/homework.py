# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lin
number_1 = 25
number_2 = 4
print(number_1 / number_2)
print(number_1 // number_2)
# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
animal = "dog"
color = "red"
print(f"A {animal} that is {color} would be cool.")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for number in range(0, 11):
    if number % 2 == 0:
        print(number)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
pushups = 20
print(pushups * 7)

# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for number in range(1, 7):
    print(f"{number} * {number} = {number ** 2}")