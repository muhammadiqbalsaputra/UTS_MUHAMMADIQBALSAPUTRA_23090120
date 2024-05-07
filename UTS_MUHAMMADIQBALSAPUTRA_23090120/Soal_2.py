# deklarasi
input_tahun = int(input('Masukan Tahun : '))

# 
if input_tahun % 400==0 or (input_tahun %4==0 and input_tahun %100!=0):
    print(f'Tahun {input_tahun} merupakan TAHUN KABISAT')
else:
    print(f'Tahun {input_tahun} BUKAN merupakan TAHUN KABISAT')
