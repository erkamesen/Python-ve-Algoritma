# Soru 20 - Başlangıç


## Soru20.1
'Kullanıcıdan 5 adet sayı alıp bunları bir array e ekleyen ardından kullanıcıya sayıları ve sayıların toplamını gösteren programı tasarlayın.'


Adımlar:
1. array modülünü arr isimi ile import et
2. arr nesnesinin array methodu ile bir array oluştur ve bir değişkene ata.
3. 5 adımlı bir for döngüsü başlat 
4. her adımda kullanıcıdan bir sayı girdisi al ve array e ekle.
5. döngüyü bitir.
6. değeri 0 olan bir değişken oluştur.
7. 5 adımlı bir döngü başlat.
8. her adımda arrayin bir indexini al ve değişkene ekle.
9. her adımda girilen sayıları kullanıcıya yansıt.r
10. toplam sonucu kullanıcıya göster. <br>
End

```
import array as arr

a = arr.array("i", [])

for i in range(5):
  a.append(int(input("Lütfen bir sayı giriniz: "))
toplam = 0
for j in range(5):
  toplam += a[j]
  print(a[j])
print(toplam)
```
## Soru20.2
'Kullanıcıdan 5 adet sayı alıp bunları bir array e ekleyen ardından kullanıcıya girilen sayıların en büyüğünü gösteren programı tasarlayın.'


Adımlar:
1. array modülünü arr isimi ile import et
2. arr nesnesinin array methodu ile bir array oluştur ve bir değişkene ata.
3. 5 adımlı bir for döngüsü başlat 
4. her adımda kullanıcıdan bir sayı girdisi al ve array e ekle.
5. döngüyü bitir.
6. değeri 0 olan en_buyuk_sayi adında bir değişken oluştur.
7. 5 adımlı bir döngü başlat.
8. her adımda arrayin bir indexini al.
9. eğer indexlenen değer en_buyuk_sayi dan büyükse en_buyuk_sayi nin değeri indexlenen değer olsun.
10. döngüyü bitir.
11. kullanıcıya en_buyuk_sayi yı çıktı olarak ver.<br>
End

```
import array as arr

a = arr.array("i", [])

for i in range(5):
  a.append(int(input("Lütfen bir sayı giriniz: "))
en_buyuk_sayi = 0
for j in range(5):
  if a[j] > en_buyuk_sayi:
    en_buyuk_sayi = a[j]
print(en_buyuk_sayi)
