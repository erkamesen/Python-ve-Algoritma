"""
'Kullanıcıdan 6 sayı alıp bunların ilk 3 ünün karesini son 3 ünün küpünü alıp ekrana sırasıyla yazan programı tasarlayın.'
"""


for i in range(6): # 0 1 2 3 4 5 -> adım sayısı = i + 1
  adim_sayisi = i + 1
  sayi = int(input("Lütfen bir sayı giriniz: "))
  if adim_sayisi < 4:
    print(sayi**2)
  else:
    pirnt("sayi**3)
