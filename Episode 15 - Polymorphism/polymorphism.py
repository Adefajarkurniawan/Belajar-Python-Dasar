class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def bersuara(self):
        print("Suara hewan tidak diketahui.")

class Kucing(Hewan):
    def bersuara(self):
        print(f"{self.nama} berkata: Meong~")

class Anjing(Hewan):
    def bersuara(self):
        print(f"{self.nama} berkata: Guk guk!")

class Burung(Hewan):
    def bersuara(self):
        print(f"{self.nama} berkata: Cuit cuit!")

hewan1 = Kucing("Kitty")
hewan2 = Anjing("Buddy")
hewan3 = Burung("Tweety")

hewan1.bersuara()
hewan2.bersuara()
hewan3.bersuara()
