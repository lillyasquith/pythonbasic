people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

age_youngest = 100
youngest_person = ""

for line in people:
    # print(line)
    parts = line.split()
    # print(parts)
    name = parts[0]
    age = int(parts[1])
    # print(f"{name} - {age}")
    

    if age < age_youngest:
        youngest_person = name
        age_youngest = age #In Python, the equals sign (=) does not mean "these two things are equal" like in math. Instead, it is an assignment operator, which means:"Take the value on the RIGHT and store it inside the variable on the LEFT.

        # The variable you want to change or update must always go on the left side of the = sign.

        #What it says: "Take the new age we just found (on the right) and save it inside our tracking variable age_youngest (on the left)

        #What happens: If age is 2 and age_youngest was 999, age_youngest becomes 2

        print(youngest_person)
        print(age_youngest)

        # IF print(f"the youngest age is {age_youngest}") is indented inside the if block, Python prints a message every single time it finds a new record-low age, rather than waiting until it finishes checking all the ages. =>> Unindent the final print statement so when it finds the lowest age, it will stop the loop and the if, and save that youngest age result to print outside the loop.

print(f"The youngest person is {youngest_person}: {age_youngest}")