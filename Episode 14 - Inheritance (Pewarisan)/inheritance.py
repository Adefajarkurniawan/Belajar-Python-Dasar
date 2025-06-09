# Class induk
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bergerak(self):
        print(f"{self.nama} sedang bergerak.")

# Class anak
class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama} berkata: Meong~")
    
    def bergerak(self):   # override method
        print(f"{self.nama} melompat-lompat.")


kucing1 = Kucing("Kitty")

kucing1.bergerak()   # akan pakai versi dari Kucing
kucing1.suara()

