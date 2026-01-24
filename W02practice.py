## Check point for W02 Practice Assignment
# f_name = input ("What is your first name?  ")
# l_name = input ("What is your last name?  ")    
# f_name = f_name.capitalize()
# l_name = l_name.capitalize()
# print (f"Your name is {l_name}, {f_name} {l_name}.")

##Team Activity for W02 Practice Assignment

# Collect user information
print ("Please enter the following information: ")
f_name = input ("First Name:  ")
l_name = input ("Last Name:  ")
email = input ("Email Address:  ")
phone = input ("Phone Number:  ")
job = input ("Job Title:  ")
id_num = input ("ID Number:  ")
hair_color = input ("Hair:  ")
eye_color = input ("Eyes:  ")
month = input ("Month:  ")
training = input ("Training(yes/no): ")

# Format names
l_name = l_name.upper()
f_name = f_name.capitalize()
job = job.title()
email = email.lower()
hair_color = hair_color.capitalize()
eye_color = eye_color.capitalize()
month = month.capitalize()
training = training.capitalize()

# Display formatted information
print (f"The ID card is: ")
print (f"---------------------------")
print (f"{l_name}, {f_name}")
print (f"{job}")    
print (f"ID: {id_num}")

print()

print (email)
print (phone)

print ()

# Additional information
print (f"Hair: {hair_color:10} Eyes: {eye_color}")
print (f"Month: {month:9} Training: {training}")
print (f"---------------------------")



