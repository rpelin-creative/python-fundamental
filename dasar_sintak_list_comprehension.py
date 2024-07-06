print('\nPerintah Del dengan list comprehension')
daftar_buku = ['Seven habits','How to Influence People','First Things First','4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list comprehension')
daftar_buku = ['Seven habits','How to Influence People','First Things First','4DX']
del daftar_buku[0:1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list comprehension A')
daftar_buku = ['Seven habits','How to Influence People','First Things First','4DX']
del daftar_buku[0:-1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list comprehension B')
daftar_buku = ['A','B','Seven habits','How to Influence People','First Things First','4DX']
del daftar_buku[0:-2] #hapus kecuali 2 isi list sebelah kanan
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list comprehension C')
daftar_buku = ['Seven habits','How to Influence People','First Things First','4DX','A','B']
del daftar_buku[0::3] #tiap 3 step hapus isi list yang pertama dihitung
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan variable list baru')
daftar_buku = ['Seven habits','How to Influence People','First Things First','4DX','A','B']
daftar_buku_baru = daftar_buku[:]
for i in range(0,len(daftar_buku_baru)):
    print (daftar_buku_baru[i])

print('\nMembuat list baru dengan variable list baru yg diambil isi list pertama')
daftar_buku = ['Seven habits','How to Influence People','First Things First','4DX','A','B']
daftar_buku_baru = daftar_buku[0:1]
for i in range(0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])

print('\nMembuat list baru dengan variable list baru yg kecuali isi list terakhir')
daftar_buku = ['Seven habits','How to Influence People','First Things First','4DX','A','B']
daftar_buku_baru = daftar_buku[0:-1]
for i in range(0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])

print('\nMembuat list baru dengan variable list baru ambil yang ganjil')
daftar_buku = ['1 Seven habits','2 How to Influence People','3 First Things First','4 4DX','5 A','6 B']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])

print('\nMembuat list baru dengan variable list baru ambil yang genap')
daftar_buku = ['1 Seven habits','2 How to Influence People','3 First Things First','4 4DX','5 A','6 B']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])

print('\nMembuat list baru dengan variable list baru ambil yang genap')
daftar_buku = ['1 Seven habits','2 How to Influence People','3 First Things First','4 4DX','5 A','6 B']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])

print('\nMembuat list baru dengan variable list baru hapus dari belakang tiap beberapa langkah')
daftar_buku = ['Seven habits','How to Influence People','First Things First','4DX','A','B']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print (daftar_buku_baru[i])