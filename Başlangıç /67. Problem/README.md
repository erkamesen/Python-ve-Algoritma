# Soru 67 - Başlangıç


## Soru 67.1

'Kullanıcıdan alınan 2 sayının toplamlarını gösteren programı tasarlayın. <br>
! Sayılar pozitif ve 50 den küçük olmalı eğer koşulları sağlamıyorsa hata döndür.'

Adımlar:
1. Kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. Eğer alınan sayılar 0 dan küçük veya 50 den büyük ise kullanıcıya hata döndür.
3. değilse sayıları topla ve sonucu ekrana çıktı olarak ver. <br>
End.

```
sayi1 = int(input("Lütfen 0-50 aralığında bir sayı giriniz: ")) # 42
sayi2 = int(input("Lütfen 0-50 aralığında bir sayı giriniz: ")) # 53

if sayi1<0 or sayi1>49 or sayi2<0 or sayi2>49:
  print("Belirtilen aralıkta bir sayı girmediniz.")
else:
  print(sayi1 + sayi2)

# Belirtilen aralıkta bir sayı girmediniz.

```


## Soru 67.2

'Kullanıcıdan alınan 2 sayının toplamlarını gösteren programı tasarlayın. <br>
! İlk sayı negatif olmalı ikinci sayı pozitif ve 20-50 aralığında olmalı eğer koşulları sağlamıyorsa hata döndür.'

Adımlar:
1. Kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. Eğer ilk sayı 0 dan küçük ve ikinci sayı 20,50 aralığında ise sayıları topla ve sonucu ekrana çıktı olarak ver.
3. değilse hata döndür. <br>
End.

```
sayi1 = int(input("Lütfen negatif bir sayı giriniz: ")) # -24
sayi2 = int(input("Lütfen 20-50 aralığında bir sayı giriniz: ")) # 32

if sayi1<0 or (sayi2<50 and sayi2>20):
  print(sayi1 + sayi2)
else:
  print("Belirtilen aralıkta bir sayı girmediniz.")

# 8

```
