"""
'Kullanıcıdan alınan sayıların ortalamasını döndüren fonksiyonu ve programı tasarlayın'
"""


def ortalama_hesapla(adim):
  toplam=0
  for i in range(sayi):
    num= int(input("Lütfen ortalama için bir sayı giriniz: "))
    toplam += num
  ortalama = toplam/adim
  return ortalama

adet=int(input("Kaç adet sayının ortalaması alınacak: "))
sonuc=ortalama_hesapla(adet)
print(sonuc)
