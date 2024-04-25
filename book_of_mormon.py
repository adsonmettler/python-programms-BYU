
# opening file and editing strings PRACTICE

# Author: Adson Mettler do Nascimento

with open("books.txt") as book_file:
    for book in book_file:
        book = book.strip("\n")

        print(book)