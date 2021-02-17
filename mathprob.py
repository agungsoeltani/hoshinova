#the machine 
def tambah():
    print('selamat datang di mesin penjumlahan silahkan masukan angka yang ingin dijumlah')
    a = int(input('masukan angka awal : '))
    b = int(input('masukan angka akhir : '))
    x = a + b
    print ('penjumalahan dari ', a ,'dan', b ,'adalah : ', x)

def kurang():
    print('selamat datang di mesin pengurangan silahkan masukan angka ynag ingin dikurang')
    a = int(input('masukan angka awal : '))
    b = int(input('masukan angka akhir : '))
    x = a - b
    print ('pengurangan dari', a ,'dan', b ,'adalah : ', x)

def discount():
    x = int(input('masukan harga awal : '))
    y = int(input('masukan diskon : '))
    z = y * x / 100
    print('jadi diskonnya adalah : ', z)


#the output n input
print('------program matematika------')
print('pilih salah satu : ')

def menu():
     math = ['[1] Penjumlahan','[2] pengurangan','[3] discount','[4] Keluar']
     for isi in math:
         print(isi)

menu()

jwb = int(input('masukan jawaban : '))

if jwb == 1:
    tambah()
elif jwb == 2:
    kurang()
elif jwb == 3:
    discount()
elif jwb == 4:
    exit()
else:
    print ('jawab yang benar!')
    exit()

