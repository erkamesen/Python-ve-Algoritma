"""
'Kullanıcıdan not bilgisini alıp not 60 veya fazla ise "Geçtiniz",
eğer küçükse aldığı notun 60 ile farkını alıp ekrana "Kaldınız, puan daha lazım." çıktısını verecek programı tasarlayın. '
"""

ders_notu = int(input("Lütfen notunuzu giriniz: "))
if ders_notu >= 60:
  print("Geçtiniz")
else:
  fark = 60 - ders_notu
  print(f"Kaldınız, {fark} puan daha lazım.")
