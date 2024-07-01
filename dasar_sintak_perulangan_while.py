"""
perulangan while
"""

jumlah_buku = 10
print(f"Jumlah buku {jumlah_buku}")

jumlah_buku_yg_sudah_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yg_sudah_dibaca}")

while jumlah_buku_yg_sudah_dibaca < jumlah_buku:
    jumlah_buku_yg_sudah_dibaca = jumlah_buku_yg_sudah_dibaca + 1
    print(f"Baca buku ke {jumlah_buku_yg_sudah_dibaca}")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yg_sudah_dibaca}")
