"""
'Kullanıcıdan kaç sayı girileceğini alıp o sayı kadar sayı girişi alıp girilen sayıların ortalamalarını kullanıcıya gösteren programı tasarlayın.'
"""

kac_sayi = int(input("Kaç adet sayı gireceksiniz: "))

toplam = 0
for i in range(kac_sayi):
  sayi = int(input("Lütfen bir sayı gir: "))
  toplam += sayi
ortalama = toplam / kac_sayi
print(ortalama)
