
print("Welcome to the shopping Cart program!")

print()

items = []
prices = []
input_option = 0

while input_option != 5:
    print()
    print("Please select one of the following: ")

    options = ["Add item", "View cart", "Remove item", "Compute total", "Quit"]

    for i in range((len(options))):
        option = options[i]

        print(f"{i + 1}. {option}")

    input_option = int(input("Please enter an action: "))

    if input_option == 1:
        # Add items
        added_item = input("What item would you like to add? ")
        items.append(added_item)

        item_price = float(input(f"What is the price of '{added_item}'? "))
        prices.append(item_price)

        print(f"'{added_item.capitalize()}' has been added to the cart.")
       

    elif input_option == 2:
        # Display cart
        print()
        print("The contents of the shopping cart are: ")

        for i in range(len(items)):
            item = items[i]
            price = prices[i]

            print(f"{i + 1}. {item.capitalize()} - ${price:.2f}")
    
    elif input_option == 3:
        # Remove item
        print()
        remove_item = int(input("Which item would you like to remove? "))
        # index number starts at 0  
        remove_item -= 1
        
        if remove_item > (len(items)):
            print("Sorry, that is not a valid item number.")
        else:
            items.pop(remove_item)
            print("Item removed.")
            prices.pop(remove_item)

    elif input_option == 4:
        # compute total
        total_price = sum(prices)
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")

    elif input_option == 5:
        print("Thank you. Goodbye.")

            
