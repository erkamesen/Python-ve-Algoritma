"""
'Kullanıcıdan alınan sayının 5 e ve 6 ya aynı anda tam bölünüp bölünmediğini kontrol eden programı tasarlayın.'
"""


sayi = int(input("Lütfen kontrol edilecek sayıyı giriniz: "))
if sayi%2==0 and sayi%3==0:
  print("Sayı 5 ve 6 ya tam bölünüyor")
else:
  print("Sayı 5 ve 6 ya tam bölünemiyor")
