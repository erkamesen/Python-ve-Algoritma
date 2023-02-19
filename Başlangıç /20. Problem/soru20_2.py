"""
'Kullanıcıdan 5 adet sayı alıp bunları bir array e ekleyen ardından kullanıcıya girilen sayıların en büyüğünü gösteren programı tasarlayın.'
"""

import array as arr

a = arr.array("i", [])

for i in range(5):
  a.append(int(input("Lütfen bir sayı giriniz: "))
en_buyuk_sayi = 0
for j in range(5):
  if a[j] > en_buyuk_sayi:
    en_buyuk_sayi = a[j]
print(en_buyuk_sayi)
