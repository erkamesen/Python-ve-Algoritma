# Soru 45 - Başlangıç


## Soru 45.1

'1 den 30 a kadar sadece tek sayıları gösteren programı tasarlayın.'



Adımlar:
1. 1 den 31 e kadar 30 adımlı bir for döngüsü başlat.
2. eğer her adımda gelen for döngüsü değişkeni 2 ye tam bölünüyorsa adımı atla.
3. eğer bölünmüyorsa değişkeni çıktı olarak ekrana yaz. <br>
End

```
for sayi in range(1,31):
  if sayi %2==0:
    continue
  else:
    print(sayi)
```


## Soru 45.2

'1 den 30 a kadar sadece çift sayıları gösteren programı tasarlayın.'



Adımlar:
1. 1 den 31 e kadar 30 adımlı bir for döngüsü başlat.
2. eğer her adımda gelen for döngüsü değişkeni 2 ye tam bölünmüyorsa adımı atla.
3. eğer bölünüyorsa değişkeni çıktı olarak ekrana yaz. <br>
End

```
for sayi in range(1,31):
  if sayi %2!=0:
    continue
  else:
    print(sayi)
```
