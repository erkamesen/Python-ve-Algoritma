"""
'Kullanıcıdan alınan 2 sayının toplamlarını gösteren programı tasarlayın.
! Sayılar pozitif ve 50 den küçük olmalı eğer koşulları sağlamıyorsa hata döndür.'
"""


sayi1 = int(input("Lütfen 0-50 aralığında bir sayı giriniz: ")) # 42
sayi2 = int(input("Lütfen 0-50 aralığında bir sayı giriniz: ")) # 53

if sayi1<0 or sayi1>49 or sayi2<0 or sayi2>49:
  print("Belirtilen aralıkta bir sayı girmediniz.")
else:
  print(sayi1 + sayi2)

# Belirtilen aralıkta bir sayı girmediniz.
