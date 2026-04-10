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
    print(f"{account_name} - ${balance}")

print()
total = sum(balances)
print(f"Total: ${total}")
average = (total / (len(balances)))
print(f"Average: ${average:.2f}")




