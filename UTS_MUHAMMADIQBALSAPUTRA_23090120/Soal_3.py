print('TOTAL BELANJAAN SEBUAH BARANG')
input_jumlah = int(input('Masukan Jumlah Barang : '))
total_belanja = 0
for jumlah in range (1,input_jumlah+1):
    harga_barang = int(input(f'Masukan Harga Barang Ke-{jumlah} : '))
    total_belanja += harga_barang

print(f'Total Belanjaan : Rp.{total_belanja:,}')