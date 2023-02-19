"""
'Basit bir artık yıl uygulaması için kullanıcıdan alınan yılın artık yıl olup olmama durumunu sadece 4 e bölünebilen cinsten tasarlayın.'
"""


year = int(input("Lütfen yılı giriniz: "))
if year %4 == 0:
  print("Artık yıl.")
else:
  print("Artık yıl değil.")
