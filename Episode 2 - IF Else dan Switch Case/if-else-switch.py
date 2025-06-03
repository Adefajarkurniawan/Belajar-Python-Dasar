nilai = int(input("Masukkan nilai: "))

# Penilaian grade menggunakan if-elif-else
if nilai >= 85:
    print("Grade: A")
elif nilai >= 70:
    print("Grade: B")
elif nilai >= 60:
    print("Grade: C")
else:
    print("Grade: D")


hari = input("Masukkan nama hari (contoh: senin): ").capitalize()

# Menggunakan match-case 
match hari:
    case "Senin":
        print("Hari Senin")
    case "Selasa":
        print("Hari Selasa")
    case "Rabu":
        print("Hari Rabu")
    case _:
        print("Hari Kamis - Minggu")

