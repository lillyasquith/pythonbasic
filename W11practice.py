
# W11 Checkpoint: Practice Opening Files

#open the file
with open("books.txt") as books:
    # read line by line
    for line in books:
        # print(line)
        # remove extra space
        cleaned_line = line.strip()
        print(cleaned_line)

# ---------------------------------------
    


