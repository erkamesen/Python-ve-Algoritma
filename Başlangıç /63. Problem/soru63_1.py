"""
'Kullanıcıdan alınan 10 adet sayıyı listeye ekleyip, liste parametresi alıp listenin
en büyük sayısını çıktı olarak veren fonksiyonla programı tasarlayın.'
"""


def max_bulucu(l):
  buyuk = 0
  for sayi in l:
    if sayi > buyuk:
      buyuk = sayi
  return buyuk

sayilar = []

for i in range(10):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayilar.append(sayi) # 33 231 1844 123 1412 12 444 2311 11132 4232

sonuc = max_bulucu(l=sayilar)
print(sonuc) # 11132
