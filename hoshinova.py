print("menghitung kecepatan rata-rata")
print("pilih pertanyaan yang ingin ditanyakan")

prt1 = ['1. ditanya kecepatan (v)', '2. ditanya jarak (s)', '3. ditanya waktu tempuh (t)']

for x in prt1:
    print(x)

prt1_q = int(input("masukan salah satu pertanyaan yang di tanyakan dengan cara masukan nomor yang benar : "))

if prt1_q == int("1"):
     a1 = float(input("masukan jarak (km) : "))
     b1 = float(input("masukan waktu tempuh (jam) : "))
     qst_v = float(a1) / float(b1)
     print("jadi kecepatan rata-ratanya adalah : ",qst_v,"km/jam")
     print("program selesai")
elif prt1_q == int("2"):
     a2 = float(input("Masukan waktu tempuh (jam) : "))
     b2 = float(input("Masukan kecepatan (km/jam) : "))
     qst_j = float(a2) * float(b2)
     print("jarak yang akan ditempuh dari waktu tempuh",a2,"jam adalah",qst_j)
     print("program selesai")
elif prt1_q == int("3"):
     a3 = float(input("Masukan jarak (km) : "))
     b3 = float(input("Masukan kecepatan(km/jam) : "))
     qst_w = float(a3) / float(b3)
     print("waktu yang dibutuhkan dari jarak",a3,"km dengan kecepatan",b3,"km/jam adalah",qst_w,"jam")
     print("program selesai")





