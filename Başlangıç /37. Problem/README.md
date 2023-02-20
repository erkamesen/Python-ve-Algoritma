# Soru 37 - Başlangıç


## Soru 37.1

'Kullanıcıdan alınan 2 sayının küplerinin toplamını bulun programı tasarlayın.'

Adımlar:
1. Kullanıcıdan 2 adet sayı alıp değişkenlere ata.
2. değişkenlerin küplerini al ve toplamlarının sonucunu bir değişkene ata.
3. sonucu ekrana yaz. <br>
End

```
sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
print(sayi1**3 + sayi2**3)
```

## Soru 37.2

'Kullanıcıdan 6 sayı alıp bunların ilk 3 ünün karesini son 3 ünün küpünü alıp ekrana sırasıyla yazan programı tasarlayın.'

Adımlar:
1. 6 adımlı bir for dmngüsü başlat
1. her adımda kullanııdan bir sayı al
3. eğer adım sayısı 4 den küçükse sayıların karesini al ve sonucu ekrana yaz.
4. değilse sayıların küpünü al ve sonucu ekrana yaz. <br>
End

```
for i in range(6): # 0 1 2 3 4 5 -> adım sayısı = i + 1
  adim_sayisi = i + 1
  sayi = int(input("Lütfen bir sayı giriniz: "))
  if adim_sayisi < 4:
    print(sayi**2)
  else:
    pirnt("sayi**3)
```
