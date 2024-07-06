"""
perulangan while
"""

book_count = 10
print(f"number of books {book_count}")

read_count = 0
print(f"Number of books read {read_count}")

understood_count = 0
print(f"Number of books read and understood {understood_count}")


while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Book {understood_count + 1} is not yet understood")
    else:
        understood_count = understood_count + 1
        print(f"Read book {understood_count}")

print(f"Number of books read {understood_count}")
if understood_count == book_count:
    print("Ma'am, all the books have been understood")
else:
    print(f"Mom, not all books can be understood,"
          f" Budi only understands {understood_count} books ")