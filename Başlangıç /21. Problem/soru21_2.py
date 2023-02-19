"""
'Kullanıcıdan 5 adet sayı alıp bunları bir array e ekleyen ardından kullanıcıya girilen sayıların en küçüğünün ve
en büyüğünün toplamını gösteren programı tasarlayın.'
"""


import array as arr

a = arr.array("i", [])

for i in range(5):
  a.append(int(input("Lütfen bir sayı giriniz: "))
en_kucuk = a[0]
en_buyuk = 0
for j in range(5):
  if en_kucuk > a[j]:
    en_kucuk = a[j]
  if en_buyuk < a[j]:
    en_buyuk = a[j]
print(en_kucuk + en_buyuk)
