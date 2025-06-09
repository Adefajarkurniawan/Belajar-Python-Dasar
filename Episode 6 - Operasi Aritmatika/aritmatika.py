try:
    f = open("data.txt")
    # kode membaca file
except FileNotFoundError:
    print("File tidak ditemukan.")
finally:
    print("Program selesai dijalankan.")
