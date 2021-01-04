harga = input("masukan harga barang : ")
prt   = input("ada diskon? y or n : ")

if prt == "y":
    diskon = input("masukan diskon : ")
elif prt == "n":
    diskon = 0

ongkir = input("masukan ongkir : ")

print ("pilih salah satu metode pembayaran dibawah : ")
print ("1. Alfamart")
print ("2. Indomaret")
print ("3. cod")
print ("4. tidak ada")

prt2 = int(input("masukan nomor metode pembayaran yang sesuai : "))

if prt2 == 1:
 pmbr = 2500
elif prt2 == 2:
 pmbr = 2500
elif prt2 == 3:
 pmbr = 3500
elif prt2 == 4:
 pmbr = 0

#proses
#perhitungan diskon
data1 = int(harga) * int(diskon)
data2 = int(data1) / 100
data3 = int(harga) - int(data2)

#proses penggabungan
data4 = int(data3) + int(ongkir)
data5 = int(data4) + int(pmbr)

#output
print ("total belanjaan yang harus di bayar adalah", data5)



