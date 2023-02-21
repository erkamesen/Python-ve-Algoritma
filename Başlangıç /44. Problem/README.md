# Soru 44 - Başlangıç


## Soru 44.1

'Kullanıcıdan alınan 2 sayıdan büyük olanından küçük olanına kadar sayılar dahil kullanıcıya yan yana şekilde gösteren programı tasarlayın.'

Adımlar:
1. 2 adet parametre alan bir fonksiyon tanımla.
-  1. parametreden 2. parametrenin bir eksiğine kadar ters şekilde ilerlicek bir for döngüsü başlat.
- her adımda for döngüsünden gelen değişkeni kullanıcıya göster.
1. Kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. eğer birinci sayı ikinci sayıdan büyükse fonksiyonun ilk parametresi birinci sayı ikinci parametresi ikinci sayı olsun.
3. eğer değilse fonksiyonun ilk parametresi ikinci sayı birinci parametresi ikinci sayı olsun. <br>
End

```
def say(buyuk_sayi, kucuk_sayi):
  for sayi in range(buyuk_sayi, kucuk_sayi-1, -1): # Ters saymak için -1 parametresi de veriyoruz.
    print(sayi, end=" ")

sayi1 = int(input("Lütfen bir sayı giriniz: ")) # 1
sayi2 = int(input("Lütfen bir sayı giriniz: ")) # 7

if sayi1 > sayi2:
  say(buyuk_sayi=sayi1, kucuk_sayi=sayi2)
else:
  say(buyuk_sayi=sayi2, kucuk_sayi=sayi1)

# 7 6 5 4 3 2 1

```

## Soru 44.2

'Kullanıcıdan alınan 2 sayıdan küçük olanından büyük olanına kadar sayılar dahil sadece tek sayıları kullanıcıya  gösteren programı tasarlayın.'

Adımlar:
1. 2 adet parametre alan bir fonksiyon tanımla.
-  1. parametreden 2. parametrenin bir fazlasına kadar ters şekilde ilerlicek bir for döngüsü başlat.
- eğer her adımda for döngüsünden gelen değişken 2 ye tam bölünüyorsa adımı atla.
- eğer tam bölünmüyorsa sayıyı kullanıcıya göster.
1. Kullanıcıdan 2 adet sayı al ve değişkenlere ata.
2. eğer birinci sayı ikinci sayıdan küçükse fonksiyonun ilk parametresi birinci sayı ikinci parametresi ikinci sayı olsun.
3. eğer değilse fonksiyonun ilk parametresi ikinci sayı birinci parametresi ikinci sayı olsun. <br>
End

```
def say(kucuk_sayi, buyuk_sayi):
  for sayi in range(kucuk_sayi, kucuk_sayi+1): 
    if sayi %2 == 0:
      continue
    else:
      print(sayi)

sayi1 = int(input("Lütfen bir sayı giriniz: ")) # 16
sayi2 = int(input("Lütfen bir sayı giriniz: ")) # 3

if sayi1 > sayi2:
  say(buyuk_sayi=sayi1, kucuk_sayi=sayi2)
else:
  say(buyuk_sayi=sayi2, kucuk_sayi=sayi1)

"""
3
5
7
9
11
13
15
"""

```
