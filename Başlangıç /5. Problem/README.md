# Soru 5 - Başlangıç

## Soru 5.1

'Kullanıcıdan 2 farklı sayıp alıp bu sayılar üzerinde tüm aritmetik işlemleri yapıp ekrana gösteren programı tasarlayın. <br>
(Toplama, Çıkarma, Bölme, Çarpma)'

Adımlar:
1. Kullanıcıdan birinci sayıyı al ve bir değişkene ata.
2. Kullanıcıdan ikinci sayıyı al ve bir değişkene ata.
3. iki değişkenin toplamını bir değişkene ata ve ekrana yaz.
4. iki değişkenin farkını bir değişkene ata ve ekrana yaz.
5. iki değişkenin bölümünü bir değişkene ata ve ekrana yaz.
6. iki değişkenin çarpımını bir değişkene ata ve ekrana yaz. <br>
End

```
sayi1 = float(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = float(input("Lütfen ikinci sayıyı giriniz: ")

toplam = sayi1 + sayi2
print(f"{sayi1} + {sayi2} = {toplam}")

fark = sayi1 - sayi2
print(f"{sayi1} - {sayi2} = {fark}")

bolum = sayi1 / sayi2
print(f"{sayi1} / {sayi2} = {bolum}")

carpim = sayi1 * sayi2
print(f"{sayi1} * {sayi2} = {carpim}")

```
## Soru 5.2

'Kullanıcıdan 3 farklı sayı alıp bunların çarpımının toplamına bölümünü ekrana çıktı olarak veren programı tasarla.'

Adımlar:
1. Kullanıcıdan birinci sayıyı al ve bir değişkene ata.
2. Kullanıcıdan ikinci sayıyı al ve bir değişkene ata.
3. Kullanıcıdan üçücü sayıyı al ve bir değişkene ata.
4. Tüm sayıları çarp ve sonucu bir değişkene ata.
5. Tüm sayıları topla ve sonucu bir değişkene ata.
6. çarpımları toplama oranla ve sonucu ekrana yaz. <br>
End

```
sayi1 = float(input("Lütfen birinci sayıyı giriniz: ")
sayi2 = float(input("Lütfen ikinci sayıyı giriniz: ")
sayi3 = float(input("Lütfen üçüncü sayıyı giriniz: ")
carpim = sayi1 * sayi2 * sayi3
toplam = sayi1 + sayi2 + sayi3
oran = carpim / toplam
print("Sonuç :", oran)
```
