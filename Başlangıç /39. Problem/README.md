# Soru 39 - Başlangıç

## Soru 39.1

'Kullanıcıdan 5 adet sayı alıp bunu listede saklayan, ardından bu listeyi parametre olarak alıp listedeki sayıların toplamını döndüren fonksiyonu ve programı tasarlayın.'

Adımlar:
1. 1 adet parametre alan bir fonksiyon tanımla:
- değeri 0 olan bir değişken tanımla.
- 5 adımlı bir döngü başlat.
- her adımda listenin bir itemini al ve değişkenin değerine ekleyerek değişkenin değerini güncelle.
- döngüyü bitir.
- sonucu döndür.
2. boş bir liste oluştur ve bir değişkene ata.
3. 5 adımlı bir döngü başlat.
4. her adımda kullanıcıdan bir sayı alıp sayıyı listeye ekle.
5. listeyi fonksiyona parametre olarak ver. 
6. sonucu ekrana yazdır. <br>
End

```
def liste_toplayici(l):
  s = 0
  for sayi in l:
    s += int(sayi):
  return s
  
sayilar = []

for i in range(5):
  sayilar.append(int(input("Lütfen bir sayı giriniz: "))

print(liste_toplayici(l=sayilar))
```

## Soru 39.2

'Kullanıcıdan 5 adet sayı alıp bunu tuple da saklayan, ardından bu tuple ı parametre olarak alıp listedeki sayıların toplamını döndüren fonksiyonu ve programı tasarlayın.'

Adımlar:
1. 1 adet parametre alan bir fonksiyon tanımla:
- değeri 0 olan bir değişken tanımla.
- 5 adımlı bir döngü başlat.
- her adımda listenin bir itemini al ve değişkenin değerine ekleyerek değişkenin değerini güncelle.
- döngüyü bitir.
- sonucu döndür.
2. boş bir tuple oluştur ve bir değişkene ata.
3. 5 adımlı bir döngü başlat.
4. her adımda kullanıcıdan bir sayı alıp sayıyı tuple a ekle.
5. tuple ı fonksiyona parametre olarak ver. 
6. sonucu ekrana yazdır. <br>
End

```
def tuple_toplayici(l):
  s = 0
  for sayi in l:
    s += int(sayi):
  return s
  
sayilar = ()

for i in range(5):
  sayilar += (int(input("Lütfen bir sayı giriniz: "), )

print(tuple_toplayici(l=sayilar))
```


