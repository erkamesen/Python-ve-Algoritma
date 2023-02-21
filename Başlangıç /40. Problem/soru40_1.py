"""
'kullanıcıdan alınan kullanıcı adının sadece harf veya rakamdan oluşup oluşmadığını kontrol eden fonksiyonla beraber programı tasarlayın.'
"""


def kontrol(kelime):
  if kelime.isalnum():
    return True
  else:
    return False

kullanici_adi = input("Lütfen bir kullanıcı adı giriniz: ")
if kontrol(kelime=kullanici_adi):
  print("Bu kullanıcı adı kullanılabilir.")
else:
  print("Bu kullanıcı adı kullanılamaz.")
