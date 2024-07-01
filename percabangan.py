# sequence
print('ibu berkata,"Pergi ke toko!"')
print('Budi menjawab,"Baik apa yang harus saya lakukan di toko?"')
print('ibu menjawab,"Beli satu botol susu, jika ada telor beli 6"')
print('Maka budi pergi ke toko')
print('Dan mulai berbelanja')

# percabangan
jumlah_botol_susu = 0
jumlah_telur =10

print(f"Jumlah Botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print('Ambil susu 1 botol')
    if jumlah_telur > 5:
        print('Ambil 6 telur')
    else:
        print('Tidak ambil telur')
else:
    print('Budi tidak jadi membeli susu')
    if jumlah_telur > 5:
        print('Ambil 6 telur')
    else:
        print('Tidak ambil telur')

print('pulang')
print('menyerahkan hasil belanja')