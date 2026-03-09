#****************************************************#
# W09 CheckPoint - Practice working with list indexes.
#****************************************************#
print("Please enter the items of the shopping list (type: quit to finish):")
items = []
item = ""

while item.lower() != "quit":
    item = input("Item: ")
    
    if item.lower() != "quit":
        items.append(item)

# Loop through the items in the regular way
print()       
print("The shopping list is:")
for item in items:
    print(item)

# Loop through the items using an index
print()
print("The shopping list with indexes is: ")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")

# Replace the item at that index with the new item
print()
remove_item = int(input("Which item would you like to change? "))
items.pop(remove_item)
new_item = input("What is the new item? ")
items.insert(remove_item, new_item)

# display the whole updated list again
print()
print("The shopping list with indexes is: ")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item}")