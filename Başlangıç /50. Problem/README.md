# Soru 50 - Başlangıç

## Soru 50.1

'Kullanıcıdan alınan taban uzunluğu ve yükseklik ile üçgenin alanını bulan programı tasarlayın. alan=(taban uzunluğu\*yükseklik)/2'

Adımlar:
1. kullanıcıdan taban uzunluğunu al ve bir değişkene ata.
2. kullanıcıdan yükseklik al ve bir değişkene ata.
3. formülde değişkenleri yerine koy ve sonucu bir değişkene ata.
4. sonucu çıktı olarak ekrana ver. <br>
End

```
taban_uzunlugu = float(input("Lütfen üçgenin taban uzunluğunu giriniz: ")) # 10
yukseklik = float(input("Lütfen üçgenin yüksekliğini giriniz: ")) # 30

alan = (taban_uzunlugu*yukseklik)/2
print(alan) # 150
```

## Soru 50.2

'Kullanıcıdan alınan taban uzunluğu ve yükseklik ile üçgenin alanını bulan ardından kullanıcıdan bir sayı alıp sayının karesini alanın değerinin üstüne ekleyen programı tasarlayın. alan=(taban uzunluğu\*yükseklik)/2'

Adımlar:
1. kullanıcıdan taban uzunluğunu al ve bir değişkene ata.
2. kullanıcıdan yükseklik al ve bir değişkene ata.
3. formülde değişkenleri yerine koy ve sonucu bir değişkene ata.
4. sonucun karesini al ve bir değişkene ata.
5. sonucu ve sonucun karesini topla ve bir değişkene ata.
6. sonucu çıktı olarak ekrana ver. <br>
End

```
taban_uzunlugu = float(input("Lütfen üçgenin taban uzunluğunu giriniz: ")) # 5
yukseklik = float(input("Lütfen üçgenin yüksekliğini giriniz: ")) # 10

alan = (taban_uzunlugu*yukseklik)/2 #25
alan_karesi = alan**2 # 625
toplam = alan + alan_karesi 
print(toplam) # 675
```
