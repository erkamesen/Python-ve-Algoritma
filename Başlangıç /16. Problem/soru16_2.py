"""
'Kullanıcıdan alınan iki sayının kendi aralarında compound(bileşik) operatörler ile işlemlerini ve sonuçlarını gösteren programı tasarlayın.
(+=, -= vb.)'
"""


sayi1 = int(input("Lütfen ilk sayı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayı giriniz: "))
print(sayi1 += sayi2) # sayi1 = sayi1 + sayi2
print(sayi1 -= sayi2) # sayi1 = sayi1 - sayi2
print(sayi1 /= sayi2) # sayi1 = sayi1 / sayi2
print(sayi1 *= sayi2) # sayi1 = sayi1 * sayi2
print(sayi1 %= sayi2) # sayi1 = sayi % sayi2
