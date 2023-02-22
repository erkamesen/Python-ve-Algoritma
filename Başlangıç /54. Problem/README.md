# Soru 54 - Başlangıç


## Soru 54.1

'Kullanıcıdan aldığı sayının faktoriyelini hesaplayan programı tasarlayın.'


Adımlar:
1. Kullanıcıdan bir sayı al ve değişkene ata
2. değeri 1 olan bir değişken oluştur.
3. 1 den kullanıcının girdiği sayının bir fazlasına kadar bir for döngüsü başlat.
4. her adımda for döngüsünden gelen değişkenler değeri 1 olan değişkeni çarp ve değerini güncelle.
5. döngüyü bitir.
6. sonucu ekrana yaz. <br>
End

```
sayi = int(input("Lütfen faktoriyeli alınacak sayıyı giriniz: ")) # 5

fak = 1
for i in range(1, sayi+1):
  fak *= i
  
print(f"{sayi} Sayısının Faktoriyeli: {fak}")
# 5 Sayısının Faktoriyeli: 120
```


## Soru 54.2

'Kullanıcıdan aldığı 5 sayının faktoriyelini hesaplayan fonksiyonla, programı tasarlayın.'


Adımlar:
1. 1 parametre alan bir fonksiyon tanımla.
- değeri 1 olan bir değişken oluştur.
- 1 den parametrenin bir fazlasına kadar olan bir for döngüsü başlat.
- her adımda for döngüsünden gelen değişkenler değeri 1 olan değişkeni çarp ve değerini güncelle.
- döngüyü bitir
- değişkeni döndür
2. 5 adımlı bir for döngüsü başlat
3. her adımda kullanıcıdan bir sayı al ve fonksiyona parametre olarak sayıyı ver.
4. her adımda fonksiyonun sonucunu ekrana yazdır. <br>
End

```

def fakt(sayi):
  fak = 1
  for i in range(1, sayi+1):
    fak *= i
  return fak
 
for i in range(5):
  sayi = int(input("Lütfen faktoriyeli alınacak sayıyı giriniz: ")) # 4 5 10 15 20
  print(fakt(sayi=sayi))
  
"""
Lütfen faktoriyeli alınacak sayıyı giriniz: 4
24
Lütfen faktoriyeli alınacak sayıyı giriniz: 5
120
Lütfen faktoriyeli alınacak sayıyı giriniz: 10
3628800
Lütfen faktoriyeli alınacak sayıyı giriniz: 15
1307674368000
Lütfen faktoriyeli alınacak sayıyı giriniz: 20
2432902008176640000
"""

```
