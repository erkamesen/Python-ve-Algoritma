"""
'Kullanıcıdan 5 adet sayı alıp bunları bir array e ekleyen ardından kullanıcıya girilen sayıların en küçüğünü gösteren programı tasarlayın.'
"""

import array as arr

a = arr.array("i", [])

for i in range(5):
  a.append(int(input("Lütfen bir sayı giriniz: "))
en_kucuk = a[0]
for j in range(5):
  if en_kucuk > a[j]:
    en_kucuk = a[j]
print(en_kucuk)
