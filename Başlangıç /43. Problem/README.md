# Soru 43 - Başlangıç



## Soru 43.1

'Kullanıcının 2 sayı alıp bu sayılar dahil aralarındaki sayılarıda kullanıcıya yan yana olcau şekilde gösteren programı tasarlayın.'


Adımlar:
1. kullanıcıdan başlangıç sayısını al ve bir değişkene ata.
2. kullanıcıdan bitiş sayısını al ve bir değişkene ata.
3. başlangıç sayısından bitiş sayısının bir fazlasına kadar ilerleyecek bir for döngüsü başlat.
4. her adımda for döngümüzün oluşturduğu değişkeni çıktı olarak ekrana ver. <br>
End

```
sayi1 = int(input("Başlangıç Sayısı: ")) # 3
sayi2 = int(input("Bitiş Sayısı: ")) # 8
for i in range(sayi1, sayi2+1): # döngüdeki son sayı sayılmadığı için +1 veriyoruz.
  print(i, end=" ")

# 3 4 5 6 7 8 
```


## Soru 43.2

'1 den 100 e kadar 4 er 4 er sayan programı tasarla.'


Adımlar:
1. 1 den başlayıp 101 de biten 100 adımlı bir for döngüsü başlat
2. eğer for döngüsünden gelen değişken 4 e tam bölünüyorsa ekrana çıktı olarak ver.
3. değilse devam et. <br>
End

```
for sayi in range(1,101):
  if sayi%4 == 0 :
    print(sayi)
  else:
    continue
"""
4
8
12
16
20
24
28
32
36
40
44
48
52
56
60
64
68
72
76
80
84
88
92
96
100
"""
```

