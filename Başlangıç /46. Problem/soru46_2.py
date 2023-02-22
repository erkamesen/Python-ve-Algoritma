"""
'Kullanıcıdan 6 adet sayı alıp bunları arraye ekleyen ardından tüm sayıların ortalamalarının 1 hariç ilk tam bölen sayısını bulan programı tasarlayın.'
"""

from array import array

toplam = 0
a = array("i", [])

for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: ")) # 1444 23 32 767645 23 52342
  a.append(sayi)
  toplam += sayi
  
ortalama = toplam/6 # 136919
bolen = 2
while True:
  if ortalama %bolen != 0:
    bolen += 1
  else:
    print(bolen)
    break
# 23
