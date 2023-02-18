"""
'Kullanıcıdan bir parola alıp parolanın harf veya rakam içeriyorsa ayrıca parola 8 haeye eşit veya daha büyükse kabul eden aksi halde hata veren programı tasarlayın.
Eğer koşullar sağlanıyorsa "şifreniz ****** kabul edilmiştir" şeklinde şifreyi gizleyerek ekrana çıktı verin.'
"""

parola = input("Lütfen parolanızı giriniz: ")
parola_uzunlugu = len(parola)
if parola_uzunlugu < 8:
  print("Lütfen 8 veya daha fazla haneli bir parola oluşturun.")
else:
  if parola.isalnum():
  print(f"Parolanız {parola_uzunlugu*'*'} başarılı şekilde oluşturuldu.")
else:
  print("Lütfen parolanızın içinde sadece harf veya rakam olsun.")
  
