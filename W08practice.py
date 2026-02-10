#**************************************#
# W08 CheckPoint - For loops 
#**************************************#

# colors = ["red", "blue", "green", "yellow"]

# for color in colors:
#     print (color)

# for number in range (1, 9):
#     print(number)

# for i in range (2, 21, 2):
#     print(i)

### Note: range(start, stop, step)


#******************************************#
#W08: Team Activity - Iterating Through Strings
#*****************************************#

##Note: Use ,end="" at the end of a print statement if we do not want the print statement to end with a new line. 

#Example:
# print("This is line one.", end="")
# print("This is line two.")

# outputs: This is line one.This is line two.

# W08: Team Activity - Code starts here:

# words = "Commitment"

# user_letter = input("What is your favorite letter? ").lower()

# for i in words:
#     if i == user_letter:
#         print("_", end="")
#     else:
#         print(i.lower(), end="")


#Stretch Challenge:

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

play_again = "yes"

while play_again == "yes":
    num = int(input("Please enter a number: "))
    for i, letter in enumerate (quote):
        #print (f"letter {letter} at index {i}")
        if i % num == 0:
            print (letter.capitalize(), end="")
        else:
            print (letter.lower(), end="")
    print()   
    play_again = input("Would you like to enter another number? ")
    
print ("Goodbye.")       
