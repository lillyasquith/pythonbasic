largest_chapters = 0
book_with_largest_chapters = ""

largest_chapeters_in_BOM = 0
book_name_with_largest_chapeters_in_BOM = ""


# At the beginning of the program, ask the user which volume of scriptures they would like to learn about (for example, Old Testament, New Testament, Book of Mormon, Doctrine and Covenants, Pearl of Great Price). Then, find the book in that volume of scripture that has the largest number of chapters.
choosen_scriptures = input("Which volume of scriptures would you like to learn about: ")
largest_chapeters_in_choosen_scriptures = 0
largest_chapeters_in_choosen_scriptures_book_name = ""


# Open the file, read through it line by line, separate the line into the appropriate pieces and display each book
with open("books_and_chapters.txt") as books:
    for line in books:
        # print(line)

        #strip extra spaces
        cleaned_line = line.strip()
        # print(cleaned_line)

        # split into pieces
        parts = cleaned_line.split(":")
        # print(parts)

        book_name = parts[0]
        chapter = int(parts[1])
        scripture = parts[2]

        # print(f"Scripture: {scripture}, Book: {book_name}, Chapters: {chapter}")


        # Find the largest number of chapters in the scriptures.
        
        # if chapter > largest_chapters:
        #     largest_chapters = chapter

            # Find the book that has the largest number of chapters in the scriptures.
            # book_with_largest_chapters = book_name

    # print(book_with_largest_chapters)
    # print(largest_chapters)

        # ==================
        # Stretch Challenge
        # only prints the books in the Book of Mormon
    #     if scripture == "Book of Mormon":
    #         print(f"{scripture}: {book_name}: {chapter}")
        
    #     # Find the book in the Book of Mormon that has the largest number of chapters.
    #         if chapter > largest_chapeters_in_BOM:
    #             largest_chapeters_in_BOM = chapter
    #             book_name_with_largest_chapeters_in_BOM = book_name

    # print(f"The book in the Book of Mormon that has the largest number of chapters is: {book_name_with_largest_chapeters_in_BOM}: {largest_chapeters_in_BOM}") 
        if choosen_scriptures.lower() in scripture.lower():
            if chapter > largest_chapeters_in_choosen_scriptures:
                largest_chapeters_in_choosen_scriptures = chapter
                largest_chapeters_in_choosen_scriptures_book_name = book_name

    print(f"{choosen_scriptures}, {largest_chapeters_in_choosen_scriptures_book_name}, {largest_chapeters_in_choosen_scriptures}")

        