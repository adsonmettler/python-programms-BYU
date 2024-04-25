# Author: Adson Mettler do Nascimento
# Practicing indexes 

items = []
item = ""

print("\nPlease, enter the items of the shopping list (type: quit once you finsih):")

while item != "quit":
    item = input("Item: ")

    if item != "quit":
        items.append(item)

print()
print("The shopping list is:")

for item in items:
    print(item)

print("\nThe shopping list with indexes is:")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")

print()
index = int(input("Which item number would you like to change? "))
new_item = input("What is the new item name? ")

items[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")

print()

