# Soru 21 - Başlangıç

## Soru 21.1

'Kullanıcıdan 5 adet sayı alıp bunları bir array e ekleyen ardından kullanıcıya girilen sayıların en küçüğünü gösteren programı tasarlayın.'


Adımlar:
1. array modülünü arr isimi ile import et
2. arr nesnesinin array methodu ile bir array oluştur ve bir değişkene ata.
3. 5 adımlı bir for döngüsü başlat 
4. her adımda kullanıcıdan bir sayı girdisi al ve array e ekle.
5. döngüyü bitir.
7. 5 adımlı bir döngü başlat.
8. her adımda arrayin bir indexini al ve alınan değeri bir değişkene ata.
9. eğer bir daha ki adımda ki indexlenen değer değişkenden küçükse değişkenin değerini indexlenen değer yap.
10. döngüyü bitir.
11. kullanıcıya değişkeni çıktı olarak ver.<br>
End

```
import array as arr

a = arr.array("i", [])

for i in range(5):
  a.append(int(input("Lütfen bir sayı giriniz: "))
for j in range(5):
  en_kucuk_sayi = a[j]
  if en_kucuk_sayi < a[j]:
    en_buyuk_sayi = a[j]
print(en_buyuk_sayi)


