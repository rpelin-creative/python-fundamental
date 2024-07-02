"""
perulangan while
"""

jumlah_buku = 10
print(f"Jumlah buku {jumlah_buku}")

jumlah_buku_yg_sudah_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yg_sudah_dibaca}")

jumlah_buku_yg_sudah_dibaca_dan_dipahami = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yg_sudah_dibaca_dan_dipahami}")


while jumlah_buku_yg_sudah_dibaca < jumlah_buku * 2:
    jumlah_buku_yg_sudah_dibaca = jumlah_buku_yg_sudah_dibaca + 1
    if jumlah_buku_yg_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke {jumlah_buku_yg_sudah_dibaca_dan_dipahami + 1} belum dipahami")
    else:
        jumlah_buku_yg_sudah_dibaca_dan_dipahami = jumlah_buku_yg_sudah_dibaca_dan_dipahami + 1
        print(f"Baca buku ke {jumlah_buku_yg_sudah_dibaca_dan_dipahami}")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yg_sudah_dibaca_dan_dipahami}")
if jumlah_buku_yg_sudah_dibaca_dan_dipahami == jumlah_buku:
    print("Bu,Semua buku sudah dipahami")
else:
    print(f"Bu, Tidak semua buku bisa dipahami,"
          f" Budi hanya memahami {jumlah_buku_yg_sudah_dibaca_dan_dipahami} buku")