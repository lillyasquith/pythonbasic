#W05 CheckPoint - Practice If statements
# Comparing Numbers
first_num = float (input ("What is the first number? "))

second_num = float (input ("What is the second number? "))


if first_num > second_num:
    print ("The first number is greater")
else:
    print ("The first number is not greater")

if first_num == second_num:
    print("The numbers are equal")
else:
    print("The numbers not are equal")

if second_num > first_num:
    print ("The second number is greater")
else:
    print ("The second number is not greater")

print() # Blank line

#Comparing Strings
my_animal = "bear"
input_animal = input("What is your favorite animal? ").lower()

if input_animal == my_animal:
    print ("That's my favorite animal too! ")
else:
    print ("That one is not my favorite. ")
