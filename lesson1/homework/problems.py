# Your variables
lucky_number = 12
hours_i_sleep = 0
fav_fruit = "pineapple"
city = "redmond"
country = "united_states"
name = "mateo"
age = 6
type_of_dog = "wiener_dog"

# Print to terminal
print("My lucky number is:", lucky_number)
print("I sleep for", hours_i_sleep, "hours")
print("My favourite fruit is", fav_fruit)
print(city)
print(country)
print("My dog's name is", name, "his age is", age, "and his type is", type_of_dog)

# Write to file
with open("output_log.txt", "w") as f:
    f.write(f"My lucky number is: {lucky_number}\n")
    f.write(f"I sleep for {hours_i_sleep} hours\n")
    f.write(f"My favourite fruit is {fav_fruit}\n")
    f.write(f"{city}\n")
    f.write(f"{country}\n")
    f.write(f"My dog's name is {name}, his age is {age}, and his type is {type_of_dog}\n")