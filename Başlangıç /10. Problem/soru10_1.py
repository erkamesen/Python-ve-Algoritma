"""
'Kullanıcıdan 6 adet sayı alıp bunların toplamını ve ortalamasını ekrana yazdıran programı tasarla.'
"""


toplam = 0
for i in range(6):
  toplam += int(input("Lütfen bir sayı giriniz"))
  
ortalama = toplam / 6
print(f"Toplam: {toplam}\tOrtalama: {ortalama}")
