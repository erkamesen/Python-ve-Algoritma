# Soru 64 - Başlangıç

## Soru 64.1

'kullanıcıdan alınan not miktarına göre aşağıda ki tabloda verilen burs miktarnı hesaplayıp kullanıcıya gösteren programı tasarlayın.
```
Not 1100'e eşitse 100% burs.
Not 1000'den büyükse 80% burs.
Not 900'den büyükse 60% burs.
Not 800'den büyükse 40% burs.
Not 700 veya 700'den büyükse 30% burs.
Not 700'den küçükse burs yok.
```
'

Adımlar:
1. kullanıcıdan bir not al ve değişkene ata.
2. eğer not 1100 ise 100% burs çıktısı ver.
3. eğer not 1000 den büyük ise 80% burs çıktısı ver.
4. eğer not 900 den büyük ise 60% burs çıktısı ver.
5. eğer not 800 den büyük ise 40% burs çıktısı ver.
6. eğer not 700 veya 700 den büyük ise 30% burs çıktısı ver.
7. eğer not 700 den küçükse burs yok çıktısı ver. <br>
End.

```
ogrenci_notu = int(input("Lütfen notunuzu giriniz: "))
if ogrenci_notu == 1100:
  print("100% burs")
elif ogrenci_notu > 1000:
  print("80% burs")
elif ogrenci_notu > 900:
  print("60% burs")
elif ogrenci_notu > 800:
  print("40% burs")
elif ogrenci_notu >= 700:
  print("30% burs")
elif ogrenci_notu < 700:
  print("burs yok")

```

## Soru 64.2
'Kullanıcıdan alınan sayıların ortalamasını döndüren fonksiyonu ve programı tasarlayın'

Adımlar:
1. 1 Adet parametre alan bir fonksiyon tanımla.
- toplam adında değeri 0 olan bir değişken oluştur.
- girilen parametre kadar bir for döngüsü başlat.
- her adımda kullanıcıdan bir sayı alıp toplam değerinin üstüne ekle.
- döngüyü bitir.
- toplam sayısını gelen parametreye göl ve sonucu bir değişkene ata.
- sonucu döndür.
2. kullanıcıdan bir sayı al ve fonksiyona parametre olarak ver.
3. sonucu ekrana çıktı olarak ver. <br>
End.

```
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
```
