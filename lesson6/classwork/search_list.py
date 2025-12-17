fruits = ["banana", "mango", "apple"]

if "banana" in fruits:
    print("found banana")
else:
    print("no bananas found")

print("Our algorithm")

found = False
index = -1

for i in range(len(fruits)):
    item = fruits[i]
    if item == "banana":
        found = True
        index = i
        break

    if found == True:
        print("Found banana at", index)
else:
    print("No bananas in our list")

