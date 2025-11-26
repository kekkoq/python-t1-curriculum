import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.

clothes = ["shirt", "pants", "hat"]
last_index = len(clothes) - 1
print(clothes[last_index])

clothes = ["shirt", "pants", "hat"]

for i in range(len(clothes) - 1, -1, -1):
    print(clothes[i])

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects = ["english", "math", "pe", "science"]
print(subjects[1])
print(subjects)
# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
errors = ["400", "401", "403", "404", "500"]
print(len(errors))
index = errors.index("403")
print(index)


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
programmingLanguages = ["python", "c++",]
randomLanguage = random.choice(programmingLanguages) 
print(randomLanguage)

# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["fish23", "HairDryer12345!", "bunnyfoot2?", "123435", "aaaaa11111!!!!!!", "LOLLIPOP1228"]
print(passwords[2])







removed = passwords.pop(0)
print(removed)


print(passwords)