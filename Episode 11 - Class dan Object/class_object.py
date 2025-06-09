class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def jalan(self):
        print(self.merk, "berjalan di jalan raya.")

mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Hitam")

mobil1.jalan()
mobil2.jalan()
