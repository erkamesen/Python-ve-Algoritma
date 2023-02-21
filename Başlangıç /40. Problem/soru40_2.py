"""
'kullanıcıdan alınan kullanıcı adının 8 karakterden daha fazla olup ayrıca sadece harf veya rakamdan oluşup oluşmadığını kontrol eden
fonksiyonla beraber programı tasarlayın.'
"""


def kontrol(kelime):
  if len(kelime) <= 8:
    return False
  else:
    if kelime.isalnum():
      return True
    else:
      return False

kullanici_adi = input("Lütfen bir kullanıcı adı giriniz: ")
if kontrol(kelime=kullanici_adi):
  print("Bu kullanıcı adı kullanılabilir.")
else:
  print("Bu kullanıcı adı kullanılamaz.")
