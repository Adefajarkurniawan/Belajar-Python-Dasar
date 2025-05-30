# for
for i in range(5):
    print("Halo, world!")


# while
angka_while = 1
while angka_while <= 5:
    print("angka_while:", angka_while)
    angka_while += 1

print("=======================")

# do while loop
angka_do = 6
while True:
    print("Angka DO:", angka_do)
    angka_do += 1
    if angka_do > 10:
        break


# Break 
print("=================")

for i in range(10):
    if i == 5:
        break
    print(i)

#Continue
for i in range(5):
    if i == 2:
        continue
    print(i)