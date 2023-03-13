"""
'Kullanıcıdan alınan 2 sayının toplamlarını gösteren programı tasarlayın.
! İlk sayı negatif olmalı ikinci sayı pozitif ve 20-50 aralığında olmalı eğer koşulları sağlamıyorsa hata döndür.'
"""


sayi1 = int(input("Lütfen negatif bir sayı giriniz: ")) # -24
sayi2 = int(input("Lütfen 20-50 aralığında bir sayı giriniz: ")) # 32

if sayi1<0 or (sayi2<50 and sayi2>20):
  print(sayi1 + sayi2)
else:
  print("Belirtilen aralıkta bir sayı girmediniz.")

# 8
