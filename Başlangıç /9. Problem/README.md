# Soru 9 - Başlangıç

## Soru 9.1

'Kullanıcıdan alınan sayının 1 den 10 a kadar olan çarpımlarını ekrana yazdıran programı tasarla.'

Adımlar:
1. Kullanıcıdan bir sayı al ve bir değişkene ata.
2. 10 adımlı bir for döngüsünü başlat 
3. kullanıcının girdiği sayıyı o an ki adım sayısıyla çarp ve ekrana yazdır.
4. adım sayısını bir arttır. <br>
End

```
sayi = int(input("Lütfen bir sayı giriniz: ") -> 12
for i in range(1,11):
  print(f"{i} x {sayi} = {i*sayi}") 
  i += 1

"""
1 x 12 = 12
2 x 12 = 24
3 x 12 = 36
4 x 12 = 48
5 x 12 = 60
6 x 12 = 72
7 x 12 = 84
8 x 12 = 96
9 x 12 = 108
10 x 12 = 120
"""
```
## Soru 9.2

'Kullanıcıdan 2 sayı alıp 1 den 10 a kadar çarpımlarını 2 tab boşlukla("\t") aynı tabloda gösteren programı tasarla.'


Adımlar:
1. Kullanıcıdan iki sayı al ve değişkene ata.
2. 10 adımlı bir for döngüsünü başlat 
3. kullanıcının girdiği sayıları o an ki adım sayısıyla çarp ve ekrana 2 tab boşluk ile yazdır.
4. adım sayısını bir arttır. <br>
End

```
sayi1 = int(input("Lütfen bir sayı giriniz: ") -> 5
sayi2 = int(input("Lütfen bir sayı giriniz: ") -> 10
for i in range(1,11):
  print(f"{i} x {sayi1} = {i*sayi1}\t\t{i} x {sayi2} = {i*sayi2} ") 
  i += 1

"""
1 x 5 = 5		  1 x 10 = 10
2 x 5 = 10		2 x 10 = 20
3 x 5 = 15		3 x 10 = 30
4 x 5 = 20		4 x 10 = 40
5 x 5 = 25		5 x 10 = 50
6 x 5 = 30		6 x 10 = 60
7 x 5 = 35		7 x 10 = 70
8 x 5 = 40		8 x 10 = 80
9 x 5 = 45		9 x 10 = 90
10 x 5 = 50		10 x 10 = 100
"""
```

