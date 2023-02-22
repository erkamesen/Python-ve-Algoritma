# Soru 47 - Başlangıç

## Soru 47.1
'Kullanıcıdan 2 adet sayı alıp sayıların karelerinin toplamını kullanıcıya gösteren programı tasarlayın.'


Adımlar:
1. Kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. sayıların karelerini al ve degiskenlere ata.
3. değişkenleri topla ve sonucu ekrana çıktı olarak ver. <br>
End

```
sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
sayi1_karesi = sayi1*sayi1
sayi2_karesi = sayi2*sayi2
toplam = sayi1_karesi + sayi2_karesi

print("Sonuç :",toplam)
```

## Soru 47.2
'Kullanıcıdan 2 adet sayı alıp sayıların küplerinin toplamını kullanıcıya gösteren programı tasarlayın.'


Adımlar:
1. Kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. sayıların küplerini al ve degiskenlere ata.
3. değişkenleri topla ve sonucu ekrana çıktı olarak ver. <br>
End

```
sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
sayi1_kupu = sayi1***3
sayi2_kupu = sayi2***3
toplam = sayi1_kupu + sayi2_kupu

print("Sonuç :",toplam)
```
