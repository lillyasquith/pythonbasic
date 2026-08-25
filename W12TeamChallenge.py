# Open the file, read through it line by line, separate the line into the appropriate pieces and display each book

largest_chapters = 0
book_with_largest_chapters = ""

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
        
        if chapter > largest_chapters:
            largest_chapters = chapter
            # Find the book that has the largest number of chapters in the scriptures.
            book_with_largest_chapters = book_name

    print(book_with_largest_chapters)
    print(largest_chapters)

       
