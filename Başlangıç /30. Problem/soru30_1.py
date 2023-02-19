"""
'Kullanıcıdan alınan sayının 2 ve 3 e aynı anda tam bölünüp bölünmediğini kontrol eden programı tasarlayın.'
"""


sayi = int(input("Lütfen kontrol edilecek sayıyı giriniz: "))
if sayi%2==0 and sayi%3==0:
  print("Sayı 2 ve 3 e tam bölünüyor")
else:
  print("Sayı 2 ve 3 e tam bölünemiyor")
