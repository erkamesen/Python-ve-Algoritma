# Soru 32 - Başlangıç

## Soru 32.1

'kullanıcıdan 2 adet sayı alıp parametre olarak 2 sayı alan ve bu sayıların büyük olanını döndüren fonksiyonu tasarlayın.'


Adımlar:
1. Kullanıcıdan 2 adet sayı girişi al ve değişkenlere ata.
2. 2 parametreli bir fonksiyon tanımla.
- eğer 1. parametre 2. parametreden büyükse 1. parametreyi döndür.
- değilse 2. parametreyi döndür.
3. sonucu ekrana yazdır. <br>
End

```
def max_sayi(n1, n2):
  if n1 > n2:
    return n1
  else:
    return n2

sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
print(max_sayi(n1=sayi1, n2=sayi2))
```

## Soru 32.2

'kullanıcıdan 2 adet sayı alıp parametre olarak 2 sayı alan ve bu sayıların küçük olanını döndüren fonksiyonu tasarlayın.'


Adımlar:
1. Kullanıcıdan 2 adet sayı girişi al ve değişkenlere ata.
2. 2 parametreli bir fonksiyon tanımla.
- eğer 1. parametre 2. parametreden küçükse 1. parametreyi döndür.
- değilse 2. parametreyi döndür.
3. sonucu ekrana yazdır. <br>
End

```
def min_sayi(n1, n2):
  if n1 < n2:
    return n1
  else:
    return n2

sayi1 = int(input("Lütfen ilk sayıyı giriniz: "))
sayi2 = int(input("Lütfen ikinci sayıyı giriniz: "))
print(min_sayi(n1=sayi1, n2=sayi2))
```
