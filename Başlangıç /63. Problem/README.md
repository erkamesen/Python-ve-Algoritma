# Soru 63 - Başlangıç

## Soru 63.1

'Kullanıcıdan alınan 10 adet sayıyı listeye ekleyip, liste parametresi alıp listenin en büyük sayısını çıktı olarak veren fonksiyonla programı tasarlayın.'


Adımlar:
1. 1 adet parametre alan bir fonksiyon tanımla:
- değeri 0 olan bir değişken tanımla.
- parametrenin içinde dolaşacak bir for döngüsü başlat.
- eğer for döngüsünden gelen değişkenin değeri tanımladığımız değişkenin değerinden büyükse büyük değeri değişkene ata.
- döngüyü bitir.
- değişkeni sonuç olarak döndür.
2. boş bir liste oluştur ve bir değişkene ata.
3. 10 adımlı bir for döngüsü başlat.
4. her adımda kullanıcıdan bir sayı alıp listeye ekle.
5. döngüyü bitir. 
6. listeyi parametre olarak fonksiyona ver ve sonucu bir değişkene ata.
7. sonucu çıktı olarak ekrana ver. <br>
End


```
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
```

## Soru 63.2

'Kullanıcıdan alınan 10 adet sayıyı listeye ekleyip, liste parametresi alıp listenin en küçük sayısını çıktı olarak veren fonksiyonla programı tasarlayın.'


Adımlar:
1. 1 adet parametre alan bir fonksiyon tanımla:
- parametrenin 0. indexini al ve bir değişkene ata
- parametrenin içinde dolaşacak bir for döngüsü başlat.
- eğer for döngüsünden gelen değişkenin değeri tanımladığımız değişkenin değerinden küçükse küçük değeri değişkene ata.
- döngüyü bitir.
- değişkeni sonuç olarak döndür.
2. boş bir liste oluştur ve bir değişkene ata.
3. 10 adımlı bir for döngüsü başlat.
4. her adımda kullanıcıdan bir sayı alıp listeye ekle.
5. döngüyü bitir. 
6. listeyi parametre olarak fonksiyona ver ve sonucu bir değişkene ata.
7. sonucu çıktı olarak ekrana ver. <br>
End


```
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
```
