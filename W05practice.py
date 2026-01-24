#W05 CheckPoint - Practice If statements
# Comparing Numbers
# first_num = float (input ("What is the first number? "))

# second_num = float (input ("What is the second number? "))


# if first_num > second_num:
#     print ("The first number is greater")
# else:
#     print ("The first number is not greater")

# if first_num == second_num:
#     print("The numbers are equal")
# else:
#     print("The numbers not are equal")

# if second_num > first_num:
#     print ("The second number is greater")
# else:
#     print ("The second number is not greater")

# print() # Blank line

#Comparing Strings
# my_animal = "bear"
# input_animal = input("What is your favorite animal? ").lower()

# if input_animal == my_animal:
#     print ("That's my favorite animal too! ")
# else:
#     print ("That one is not my favorite. ")


#---------------------------------
# Team Activity - Grade Calculator

user_grade = int (input ("What is your grade percent? "))

letter = ""

if user_grade >= 90:
    letter = "A"
elif user_grade >= 80:
    letter = "B"
elif user_grade >= 70:
    letter = "C"
elif user_grade >= 60:
    letter = "D"
elif user_grade < 60:
    letter = "F"
else:
    print("Please enter a valid number.")

# STRETCH CHALLENGE:
#Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-. For each grade, you'll know it is a "+" if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.

#==> USE the modulo operator (%) to find the remainder after division (last digit checks). 

sign = ""

user_grade_with_sign = user_grade % 10

if user_grade_with_sign >= 7:
    sign = "+"
elif user_grade_with_sign < 3:
    sign = "-"
else:
    sign = ""

# Have a single print statement that prints the letter grade once.
print (f"Your grade is {letter}{sign}.")

#Check  if the user passed the course
if user_grade >= 70:
    print ("Congrats! You passed the class.")
else:
    print (f"Unfotunately, you did not pass the class. Better luck next time!")

