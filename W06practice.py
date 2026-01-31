#W06 CheckPoint - Qualifying for a Loan

# print ("Rating from 1-10 on the following:")
# loan_amount = int (input ("How large is the loan? "))

# credit_history = int (input ("How good is your credit history? "))

# income = int (input ("How high is your income? "))

# down_payment = int (input ("How large is your down payment? "))

# If logic

# Create a boolean variable for whether you should loan the money that will be set to False
# should_loan = False

# if loan_amount >= 5:
#     if credit_history >= 7 and income >= 7:
#         should_loan = True
#     elif credit_history >= 7 or income >= 7:
#         if down_payment >= 5:
#             should_loan = True
#         else:
#             should_loan = False
#     else:
#         should_loan = False
# elif loan_amount < 5:
#     if credit_history < 4:
#         should_loan = False
#     else:
#         if income >= 7 or down_payment >= 7:
#             should_loan = True
#         elif income >= 4 and down_payment >= 4:
#             should_loan = True
#         else:
#             should_loan = False
        
# if should_loan == True:
#     print ("Decision: 'yes'")
# else:
#     print ("Decision: 'no'")

# _____________________________________________
#06 Teach: Team Activity - Amusement Park Rides

age_first = int(input("What is the age of the first rider? "))

height_first = int(input("What is the height of the first rider? "))

second_rider = input("Is there a second rider (yes/no)? ")
second_rider = second_rider.lower()

can_ride = False

if second_rider == "no":
    if age_first >= 18 and height_first >= 62:
        can_ride = True
    else:
        can_ride = False
else: # Having a second rider
    age_second = int(input("What is the age of the second rider? "))
    height_second = int(input("What is the height of the second rider? "))
    if (age_first >= 18 or age_second >=18) and (height_first >= 36 and height_second >= 36):
        can_ride = True
    else:
        can_ride = False

if can_ride == True:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")





