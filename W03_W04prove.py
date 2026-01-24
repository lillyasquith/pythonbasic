child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
total_children = int(input("How many children are there? "))
total_adult = int(input("How many adults are there? "))
tax_rate = float(input("What is the sales tax rate? "))

sub_total = (child_meal * total_children) + (adult_meal * total_adult)
print(f"Subtotal: ${sub_total}")

sale_tax = round(((sub_total * tax_rate) / 100),2)
print(f"Sales Tax: ${sale_tax}")

total = round((sub_total + sale_tax),2)
print(f"Total: ${total}")

payment_amount = float(input("What is the payment amount? "))
change = round((payment_amount - total),2)
print(f"Change: ${change}")