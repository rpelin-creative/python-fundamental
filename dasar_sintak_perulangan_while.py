"""
perulangan while
"""

book_count = 10
print(f"Jumlah buku {book_count}")

read_count = 0
print(f"Jumlah buku yang sudah dibaca {read_count}")

understood_count = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {understood_count}")


while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Buku ke {understood_count + 1} belum dipahami")
    else:
        understood_count = understood_count + 1
        print(f"Baca buku ke {understood_count}")

print(f"Jumlah buku yang sudah dibaca {understood_count}")
if understood_count == book_count:
    print("Bu,Semua buku sudah dipahami")
else:
    print(f"Bu, Tidak semua buku bisa dipahami,"
          f" Budi hanya memahami {understood_count} buku")