"""
'Kullanıcıdan alınan 2 sayıdan küçük olanından büyük olanına kadar sayılar dahil sadece tek sayıları kullanıcıya gösteren programı tasarlayın.'
"""


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
