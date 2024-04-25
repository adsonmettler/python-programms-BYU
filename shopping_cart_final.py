## SHOPPING CART program ##

# Author: Adson Mettler do Nascimento

####### EXCEEDING ACTIVITY #########
# I added in the menu option 3 (Remove item) an message error in case the user input the item name instead of the item number,
# or if the user input anything else that not corresponds to the items of the shopping cart.

menu_list = ["Add item", "View shopping cart","Remove item","Compute total", "Quit"]
item_list = []
price_list = []

print("\nWELCOME TO SHOPPING CART")
print("=========================")

while True:
    print("\nHere is the menu option:\n")
    for i, menu_item in enumerate(menu_list):
        print(f"{i + 1}. {menu_item}.")

    menu_item = input("\nPlease, type the menu option number you want: ")

    if menu_item == "1":
        print()
        item_added = input("What item would you like to add? Type an item name? ")
        item_list.append(item_added)
        item_price = float(input(f"What is the price of '{item_added}'? "))
        price_list.append(item_price)
        print(f"\nThe '{item_added}' has been added to your shopping cart.\n")

    elif menu_item == "2":
        print()
        print("==================================================================================")
        print("Of course! Here is your shopping cart list:\n")
        
        for i, (item, price) in enumerate(zip(item_list, price_list)):
            print(f"{i + 1}. {item} - ${price:.2f}")

    elif menu_item == "3":
        print()
        item_index = (input("Which item would you like to remove? "))
        try:
            item_index = int(item_index)
            if 1 <= item_index <= len(item_list):
                item_removed = item_list.pop(item_index - 1)
                price_removed = price_list.pop(item_index - 1)
                print(f"Item '{item_removed}' has been removed from your shopping cart.")
            else:
                print(f"Sorry, '{item_index}' is not in your shopping cart.")
        except ValueError:
            print("\n\n*******************************************************************************************************")
            print("Invalid input. Please, enter an index number related to the item you want to remove.")
            print("*******************************************************************************************************")

    elif menu_item == "4":
        print()
        running_total = 0
        
        for price_total in price_list:
            running_total = running_total + price_total

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
        print(f"The total price of your shopping cart is: ${running_total:.2f}")

    elif menu_item == "5":
        print("\nThank you for shopping with us!")
        print("Have a great day!")
        print()
        break

    else:
        print("\n\n*******************************************************************************************************")
        print("Invalid menu option! Please, try again!")
        print("*******************************************************************************************************")
        print()
        

