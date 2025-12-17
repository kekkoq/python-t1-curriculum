import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.
brands = ["ferrari", "toyoya", "honda", "bmw"]
print(brands[0])
print(brands[3])
brands.append("volswagen")
print(brands)

# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.
numberlist = ["1", "2", "3", "4", "5"]
print(numberlist[2])
numberlist.append("6")
print(numberlist)

# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then remove one city and print the updated list.
cities = ["seattle", "la", "chicago"]
print(len(cities))
cities.remove("seattle")
print(cities)

# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
extentions = [".docx", ".pdf", ".jpg", ".png", ".xlsx",".pptx"]


# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then count how many times a specific name appears.