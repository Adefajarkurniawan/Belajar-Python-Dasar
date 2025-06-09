class KarakterGame:
    def __init__(self, nama, nyawa, level):
        self.nama = nama
        self.nyawa = nyawa
        self.level = level

    def jalan(self):
        print(f"{self.nama} sedang berjalan.")

    def naik_level(self):
        self.level += 1
        print(f"Level : {self.level}")

# Membuat object
karakter1 = KarakterGame("AldiHero", 100, 1)

# Panggil method
karakter1.jalan()
karakter1.naik_level()
karakter1.naik_level()
