def make_greeting():
    greeting = "Hello world!"
    return greeting
print(make_greeting())


def build_face():
    message = make_greeting()
    return message

print(build_face())

def personalized_greeting(name):
    print("Hello", name)
personalized_greeting("John")

def rectangle_area(length, width):
    area = length * width
    return area
print(rectangle_area(3,4))

area = 67
print(area)

print(rectangle_area(3,4))

def adopt_dog():

    pet = "a dog"
    print("the pet is", pet)
    return pet
print(adopt_dog())

pet = "a cat"

def print_pet():
    prt = "a dog"
    print(pet)

print_pet()
print(pet)

pet = "horse"

def print_horse():
    global pet
    pet = "not horse"
    print(pet)
print_horse()
print(pet)