
buah = ["apel", "jeruk", "mangga"]

print(buah[0])

#menambahkan elemen ke list
buah = ["apel", "jeruk", "mangga"]

buah.append("pisang")
print(buah)

#mengubah elemen ke list
buah = ["apel", "jeruk", "mangga"]

buah.append("pisang")

jeruk = buah.index("jeruk")
buah[jeruk] = "durian"
print(buah)