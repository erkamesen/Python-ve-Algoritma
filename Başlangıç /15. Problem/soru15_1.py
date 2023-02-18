"""
'Kullanıcıdan 6 adet sayı alıp listeye ekleyen ve listeyi ilk düz ardından ters şekilde kullanıcıya gösteren programı tasarlayın.'
"""

sayi_listesi = []
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayi_listesi.append(sayi)
print(sayi_listesi)
print(sayi_listesi[::-1])
