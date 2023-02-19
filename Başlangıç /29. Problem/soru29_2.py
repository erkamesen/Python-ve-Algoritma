"""
'Kullanıcıdan alınan sayının negatif mi pozitif mi yada sıfır mı olduğunu kontrol eden programı tasarlayın.'
"""


sayi = int(input("Lütfen kontrol edilecek sayıyı giriniz: ")
if sayi < 0:
  print(f"{sayi} Negatif")
elif sayi == 0:
  print(f"{sayi} Sıfır")
else:
  print(f"{sayi} Pozitif")
