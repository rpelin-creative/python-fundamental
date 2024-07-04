daftar_buku = ['Seven habits','How to Influence People','First Things First','4DX']
print('Tampilkan variable daftar_buku')
print(daftar_buku)

print('\nAmbil data menggunakan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku berdasarkan index tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji volume 2', -345, 3.14]
print('\nTampilkan dengan for in range dengan isi type data berbeda beda ')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Aku','Bandung','Cacing','Dodol']
print('\ndaftar_buku setelah di append')
daftar_buku.append('Endog')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])


print('\nAmbil data dan hapus isi list Pakai pop dari kiri')
daftar_buku = ['Aku','Bandung','Cacing','Dodol']
buku1 = daftar_buku.pop(0)
buku2 = daftar_buku.pop(1)
buku3 = daftar_buku.pop(1)
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nHasil pop dari kiri yg diambil')
print(buku1)
print(buku2)
print(buku3)

print('\nAmbil data dan hapus isi list Pakai pop dari kanan')
daftar_buku = ['Aku','Bandung','Cacing','Dodol']
buku1 = daftar_buku.pop(-1)
buku2 = daftar_buku.pop(-3)
buku3 = daftar_buku.pop(-1)
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nHasil pop dari kanan yg diambil')
print(buku1)
print(buku2)
print(buku3)