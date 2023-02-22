# Soru 57 - Başlangıç

## Soru 57.1

'Kullanıcıdan kaç sayı girileceğini alıp o sayı kadar sayı girişi alıp girilen sayıların ortalamalarını kullanıcıya gösteren programı tasarlayın.'

Adımlar:
1. kullanıcıdan bir sayı girişi al ve değişkene ata.
2. değeri 0 olan bir değişken oluştur.
3. kullanıcının girdiği sayı kadar adımlı bir for döngüsü başlat.
4. her adımda kullanıcıdan bir sayı al ve değeri 0 olan değişkenin üstüne ekle.
5. döngüyü bitir.
6. toplam sonucu adım sayısına böl ve sonucu bir değişkene ata.
7. sonucu kullanıcıya göster. <br>
End

```
kac_sayi = int(input("Kaç adet sayı gireceksiniz: "))

toplam = 0
for i in range(kac_sayi):
  sayi = int(input("Lütfen bir sayı gir: "))
  toplam += sayi
ortalama = toplam / kac_sayi
print(ortalama)
```
## Soru 57.2

'Kullanıcıdan alınan cümle içinde " " karakterleri hariç kaç karakterli olduğunu hesaplayan prgoramı tasarlayın.'

Adımlar:
1. kullanıcıdan bir cümle al ve değişkene ata.
2. değeri 0 olan bir değişken oluştur.
3. cümlenin içinde dolaşacak bir for döngüsü başlat.
4. eğer for döngüsünden gelen değişken " " ise adımı atla
5. değilse değeri 0 olan değişkenin değerini 1 arttır.
6. toplam değeri kullanıcıya göster. <br>
End

```
cumle = input("Lütfen bir cümle giriniz: ") # Python yüksek seviye ve nesne yönelimli bir dildir.

toplam = 0
for karakter in cumle:
  if karakter == " ":
    continue
  else:
    toplam +=1
print(toplam) # 43
```

