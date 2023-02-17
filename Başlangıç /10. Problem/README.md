# Soru 10 - Başlangıç

## Soru 10.1

'Kullanıcıdan 6 adet sayı alıp bunların toplamını ve ortalamasını ekrana yazdıran programı tasarla.'

Adımlar:
1. toplam adında 0 değerinde bir değişken oluştur.
2. 6 adımlık bir for döngüsü başlat.
3. kullanıcıdan bir sayı bilgisi al.
4. toplam değişkeninin değerini girilen sayı kadar arttır.
5. adım sayısı 6 olduysa döngüyü bitir, olmadıysa 3. adıma geri dön.
6. toplamı 6 ile böl ve sonucu bir değişkene ata.
7. ekrana toplamı ve ortalamayı yazdır. <br>
End

```
toplam = 0
for i in range(6):
  toplam += int(input("Lütfen bir sayı giriniz"))
  
ortalama = toplam / 6
print(f"Toplam: {toplam}\tOrtalama: {ortalama}")
```

## Soru 10.2

'Kullanıcıdan alınan 10 sayının karesini sırasıyla ekrana yazdıran programı tasarla'

Adımlar:
1. 10 adımlık bir for döngüsü başlat.
2. kullanıcıdan bir sayı bilgisi al.
3. girilen sayının karesini ekrana yazdır.
4. adım sayısı 10 olduysa döngüyü bitir, olmadıysa 2. adıma geri dön.
End

```
for i in range(10):
  sayi = int(input("Lütfen karesi alınacak sayıyı giriniz: ") -> 3, 4, 2, 5, 8, 11, 15, 6, 10, 9
  print(f"Sayının Karesi: {sayi**2}"
"""
Lütfen karesi alınacak sayıyı giriniz: 3
Sayının Karesi: 9
Lütfen karesi alınacak sayıyı giriniz: 4
Sayının Karesi: 16
Lütfen karesi alınacak sayıyı giriniz: 2
Sayının Karesi: 4
Lütfen karesi alınacak sayıyı giriniz: 5
Sayının Karesi: 25
Lütfen karesi alınacak sayıyı giriniz: 8
Sayının Karesi: 64
Lütfen karesi alınacak sayıyı giriniz: 11
Sayının Karesi: 121
Lütfen karesi alınacak sayıyı giriniz: 15
Sayının Karesi: 225
Lütfen karesi alınacak sayıyı giriniz: 6
Sayının Karesi: 36
Lütfen karesi alınacak sayıyı giriniz: 10
Sayının Karesi: 100
Lütfen karesi alınacak sayıyı giriniz: 9
Sayının Karesi: 81
"""
```

