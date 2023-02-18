"""
'Kullanıcıdan 6 adet sayı alıp tuple a ekleyen ve ardından tuple ı ilk kullanıcıya gösterdikten sonra temizleyen programı tasarlayın.'
"""


sayi_demeti = tuple()
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayi_demeti += (sayi,)
print(sayi_demeti)
sayi_demeti.clear()
