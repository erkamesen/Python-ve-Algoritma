"""
'Kullanıcıdan alınan 10 adet sayıyı listeye ekleyip, liste parametresi alıp listenin
en küçük sayısını çıktı olarak veren fonksiyonla programı tasarlayın.'
"""


def min_bulucu(l):
  kucuk = l[0]
  for sayi in l:
    if sayi < kucuk:
      kucuk = sayi
  return kucuk

sayilar = []

for i in range(10):
  sayi = int(input("Lütfen bir sayı giriniz: "))
  sayilar.append(sayi) # 33 231 1844 123 1412 12 444 2311 11132 4232

sonuc = min_bulucu(l=sayilar)
print(sonuc) # 12
