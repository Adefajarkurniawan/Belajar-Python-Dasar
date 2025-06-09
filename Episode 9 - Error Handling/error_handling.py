try:
    angka = int(input("Masukkan Angka: "))
    hasil = 10 / angka 

except ZeroDivisionError:
    print("Error : angka tidak bisa di bagi oleh 0")

except ValueError:
    print("Error : Input harus berupa angka.")

else:
    print("Hasilnya adalah ", hasil)

finally:
    print("Program Selesai")
