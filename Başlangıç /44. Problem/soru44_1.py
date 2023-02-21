"""
'Kullanıcıdan alınan 2 sayıdan büyük olanından küçük olanına kadar sayılar dahil kullanıcıya yan yana şekilde gösteren programı tasarlayın.'
"""


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
