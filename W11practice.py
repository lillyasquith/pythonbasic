
# W11 Checkpoint: Practice Opening Files

# open the file
# with open("books.txt") as books:
#     # read line by line
#     for line in books:
#         # print(line)
#         # remove extra space
#         cleaned_line = line.strip()
#         print(cleaned_line)

# ---------------------------------------
    


# W11 Team Activity

# open the file
with open("hr_system.txt") as employees:

# read through it line by line
    for line in employees:
        # print(line)
        cleaned_line = line.strip()
        # print(cleaned_line)

        # split the line into parts 
        parts = line.split()
        # print(parts)
        name = parts[0]
        id_num = parts[1]
        job_title = parts[2]
        salary = float(parts[3])
        # change the display
        # print(f"Name: {name}, Title: {job_title}")

        # ---------------------
        # Stretch Challenge

        # Display all four values in this format: name (ID: id_number), job_title - $salary.
        # print(f"{name} (ID: {id_num}), {job_title} - ${salary:.2f}")

        # calculate and display a paycheck amount for the employee. Assume that they are paid twice a month. add $1000 bonuses for anyone who is an engineer.

        paycheck = (salary / 12) / 2
        if job_title == "Engineer":
            paycheck += 1000

        print(f"{name} (ID: {id_num}), {job_title} - ${paycheck:.2f}")

