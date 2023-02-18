"""
'Kullanıcıdan bir parola alıp parolanın harf veya rakam içeriyorsa kabul eden aksi halde hata veren programı tasarlayın.
Eğer koşullar sağlanıyorsa "şifreniz ****** kabul edilmiştir" şeklinde şifreyi gizleyerek ekrana çıktı verin.'
"""

parola = input("Lütfen bir parola giriniz: ")
if parola.isalnum():
  print(f"Parolanız {len(parola)*'*'} başarılı şekilde oluşturuldu.")
else:
  print("Lütfen parolanızın içinde sadece harf veya rakam olsun.")
