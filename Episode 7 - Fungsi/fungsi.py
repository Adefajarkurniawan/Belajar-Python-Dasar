#tidak menggunakan parameter
def nama():
    print("Nama ani")

nama()
nama()

#tidak menggunakan parameter
def nama(nama):
    print("Nama ani", nama)

nama("andi")
nama("ani")

#keyword return
def tambah(a,b):
    return a + b

hasil = tambah(2,3)
print("Hasil pertambahan : ", hasil)