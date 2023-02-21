"""
'Kullanıcıdan 5 adet sayı alıp bunu listede saklayan, ardından bu listeyi parametre olarak alıp
listedeki sayıların toplamını döndüren fonksiyonu ve programı tasarlayın.'
"""

def liste_toplayici(l):
  s = 0
  for sayi in l:
    s += int(sayi):
  return s
  
sayilar = []

for i in range(5):
  sayilar.append(int(input("Lütfen bir sayı giriniz: "))

print(liste_toplayici(l=sayilar))
