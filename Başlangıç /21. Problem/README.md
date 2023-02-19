# Soru 21 - Başlangıç

## Soru 21.1

'Kullanıcıdan 5 adet sayı alıp bunları bir array e ekleyen ardından kullanıcıya girilen sayıların en küçüğünü gösteren programı tasarlayın.'


Adımlar:
1. array modülünü arr isimi ile import et
2. arr nesnesinin array methodu ile bir array oluştur ve bir değişkene ata.
3. 5 adımlı bir for döngüsü başlat 
4. her adımda kullanıcıdan bir sayı girdisi al ve array e ekle.
5. döngüyü bitir.
7. arrayin bir indexini al ve alınan değeri bir değişkene ata.
8. 5 adımlı bir döngü başlat
9. eğer güncel adımda ki indexlenen değer değişkenden küçükse değişkenin değerini indexlenen değer yap.
10. döngüyü bitir.
11. kullanıcıya değişkeni çıktı olarak ver.<br>
End

```
import array as arr

a = arr.array("i", [])

for i in range(5):
  a.append(int(input("Lütfen bir sayı giriniz: "))
en_kucuk = a[0]
for j in range(5):
  if en_kucuk > a[j]:
    en_kucuk = a[j]
print(en_kucuk)
```
## Soru 21.2

'Kullanıcıdan 5 adet sayı alıp bunları bir array e ekleyen ardından kullanıcıya girilen sayıların en küçüğünün ve en büyüğünün toplamını gösteren programı tasarlayın.'


Adımlar:
1. array modülünü arr isimi ile import et
2. arr nesnesinin array methodu ile bir array oluştur ve bir değişkene ata.
3. 5 adımlı bir for döngüsü başlat 
4. her adımda kullanıcıdan bir sayı girdisi al ve array e ekle.
5. döngüyü bitir.
6. en büyük sayıyı bulmak için değeri 0 olan bir değişken oluştur.
7. arrayin bir indexini al ve alınan değeri bir değişkene ata.
8. 5 adımlı bir döngü başlat
9. eğer güncel adımda ki indexlenen değer değişkenden küçükse değişkenin değerini indexlenen değer yap.
10. eğer indexlenen değer en büyük sayıyı oluşturmak için oluşturduğumuz değişkenin değerinden fazlaysa değişkenin değerini indexlenen değer yap.
10. döngüyü bitir.
11. en küçük sayı ile en büyük sayıyı topla ve sonucu ekrana yaz.<br>
End


```
import array as arr

a = arr.array("i", [])

for i in range(5):
  a.append(int(input("Lütfen bir sayı giriniz: "))
en_kucuk = a[0]
en_buyuk = 0
for j in range(5):
  if en_kucuk > a[j]:
    en_kucuk = a[j]
  if en_buyuk < a[j]:
    en_buyuk = a[j]
print(en_kucuk + en_buyuk)
```
