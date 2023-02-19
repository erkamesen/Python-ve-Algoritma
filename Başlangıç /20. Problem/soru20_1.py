"""
'Kullanıcıdan 5 adet sayı alıp bunları bir array e ekleyen ardından kullanıcıya sayıları ve sayıların toplamını gösteren programı tasarlayın.'
"""

import array as arr

a = arr.array("i", [])

for i in range(5):
  a.append(int(input("Lütfen bir sayı giriniz: "))
toplam = 0
for j in range(5):
  toplam += a[j]
  print(a[j])
print(toplam)
