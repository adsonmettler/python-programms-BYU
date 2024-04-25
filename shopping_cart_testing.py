## SHOPPING CART program ##

# Author: Adson Mettler do Nascimento



menu_list = ["Add a new item", "Display the contents of the shopping cart", "Quit"]
new_item = []
price = []

print("\nWELCOME TO SHOPPING CART")
print("=========================")

while True:
    print("\nHere is the menu option:")
    for i, menu_item in enumerate(menu_list):
        print(f"{i}. {menu_item}.")

    menu_item = input("Please, type the menu option number you want: ")

    if menu_item == "0":
        print()
        item_added = input("Great! Which item would you like to add? Type the name: ")
        new_item.append(item_added)
        print("\nThe new item added to your shopping list is:\n")
        
        for item in new_item:
            print(item)
            print()

    elif menu_item == "1":
        print()
        print("Of course! Here is the list of items in our store:")
        print("Socks")
        print("Jacket")
        print("pants")
        print("Shoes")
        print("T-shirt")
        print("Gloves")
        print("Hat")

    elif menu_item == "2":
        print("\nBye! It was great to have you in my store!")
        print("Have a great day!")
        print()
        break

    else:
        print("Invalid menu option. Please try again.")