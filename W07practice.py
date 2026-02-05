#**************************************#
# W07 CheckPoint - While loops 
#**************************************#



#1.Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number

# input_number = -1

# while input_number < 0:

#     input_number = int(input("Please type a positive number: "))
#     if input_number < 0:
#         print ("Sorry, that is a negative number. Please try again.")
#     else:
#         print (f"The number is: {input_number}")


#-------------------------------------#
#2.Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you."

# candy_permission = "no"

# while candy_permission == "no":

#     candy_permission = input("May I have a piece of candy? ").lower()
    
# print ("Thank you.")




#******************************************#
#W07: Team Activity - Guess My Number Game
#*****************************************#

import random

magic_number = random.randint(1,10)

# magic_number = int(input("What is the magic number? "))

guess_number = 0

#Stretch Challenge 1: Keep track of how many guesses the user has made and inform them of it at the end of the game.

count = 0

#Stretch Challenge 2: After the game is over, ask the user if they want to play again. Then, loop back and play the whole game again and continue this loop as long as they keep saying "yes".

play_again = ""

while guess_number != magic_number or play_again == "yes":
    guess_number = int(input("What is your guess? "))
    count += 1
    if guess_number > magic_number:
        print("Lower")
    elif guess_number < magic_number:
        print("Higher")
    else:
        print("You guessed it!")
        print(f"Total guesses: {count}.")
        play_again = input("Would you like to play again (yes/no)? ")
       



