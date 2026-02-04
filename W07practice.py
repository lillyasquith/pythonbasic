# W07 CheckPoint - While loops 

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

candy_permission = "no"

while candy_permission == "no":

    candy_permission = input("May I have a piece of candy? ").lower()
    
print ("Thank you.")




