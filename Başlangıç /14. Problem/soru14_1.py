"""
'Kullanıcıdan 6 sayı alıp bunları liste şeklinde ve toplamlarını gösteren programı tasarlayın.'
"""

sayi_listesi = []
toplam = 0
for i in range(6):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayi_listesi.append(sayi)
  toplam += sayi
print(f"Liste:\n{sayi_listesi}\nToplam: {toplam}")
