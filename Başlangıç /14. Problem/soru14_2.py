"""
'Kullanıcıdan 8 sayı alıp bunları tuple şeklinde ve toplamlarını gösteren programı tasarlayın.'
"""

sayi_demeti = tuple()
toplam = 0
for i in range(8):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayi_demeti += (sayi, )
  toplam += sayi
print(f"Tuple:\n{sayi_listesi}\nToplam: {toplam}")
