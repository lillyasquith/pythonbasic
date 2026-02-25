#*********************************************#
# W09 CheckPoint - Practice working with lists.
#*********************************************#

# friends = []
# name_input = ""
# while name_input.lower() != "end":
#     name_input = input("Type the name of a friend: ").capitalize()
#     if name_input.lower() != "end":
#         friends.append(name_input)
# print()
# print("Your friends are: ")
# for friend in friends:
#     print(friend)
        


#******************************************#
#W09: Team Activity - Lists of Numbers
#*****************************************#

print("Enter a list of number, type 0 when finished.")

numbers = []

number = -1

while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)
        num_of_values = len(numbers)
        for number in numbers:
            total = sum(numbers)
            average= total/num_of_values
            largest = max(numbers)
            sorted_list = sorted(numbers)

print(f"The sum is: {total}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
# print(numbers)

# ------------Stretch Challenge ----------

print(f"The smallest positive number is: {min(n for n in numbers if n>0)} ")
print(f"The sorted list is: ")
for i in sorted_list:
    print(i)