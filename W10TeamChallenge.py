#***********************************#
#W10: Team Activity - Multiple Lists
#***********************************#

account_names = []

balances = []

print("Enter the names and balances of bank accounts (type: quit when done)")

user_account = ""

while user_account.lower() != "quit":
    user_account = input("What is the name of this account? ")
    if user_account != "quit":
        account_names.append(user_account)
        input_balance = float(input("What is the balance? "))
        balances.append(input_balance)

print()
print("Account Information:")
for i in range(len(account_names)):
    account_name = account_names[i]
    balance = balances[i]
    print(f"{i}. {account_name} - ${balance}") 

print()
total = sum(balances)
print(f"Total: ${total}")
average = (total / (len(balances)))
print(f"Average: ${average:.2f}")

# Stretch Challenge 1: find the highest balance

highest_balance = max(balances)
index = balances.index(highest_balance)
highest_account = account_names[index]

print(f"Highest balance: {highest_account} - ${highest_balance}")


# Stretch Challenge 2: 
# ask the user if they want to update an account. 
update_option = "yes"

# Change the last step into a loop, so that the user can keep updating accounts until they say no. After each update, display the new list of balances.

while update_option == "yes":
    # If they respond with yes, ask for the index of the account, and the new balance.
    update_option = input("Do you want to update an account? ")
    if update_option == "yes":
        # update_index = int(input("What account index do you want to update? "))
        # new_balance = float(input("What is the new amount? "))
        # # Go to the list named balances, find the slot at update_index, and replace whatever is currently there with new_balance
        # balances[update_index] = new_balance


        # OR USE THE POP AND INSERT FUNCTIONS:
        update_index = int(input("What account index do you want to update? "))
        balances.pop(update_index)
        new_balance = float(input("What is the new amount? "))
        balances.insert(update_index, new_balance)


    print()
    print("Account Information:")
    for i in range(len(account_names)):
        account_name = account_names[i]
        balance = balances[i]
        print(f"{i}. {account_name} - ${balance}") 







