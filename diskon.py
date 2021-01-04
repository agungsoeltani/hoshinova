print("ini adalah program penghitung diskon sederhana")
#input
hargaawal   = input ("masukan harga awal : ")
diskonkamu  = input ("masukan diskon : ")
print ("proses........")

#proses
proses  = float(hargaawal) * float(diskonkamu)
proses2 = float(proses) / 100
diskon  = float(hargaawal) - float(proses2)

#output
print ("kamu mendapatkan diskon sebesar", diskonkamu,"%, kamu harus membayar", float(diskon))