"""
'Kullanıcıdan giriş için alınan kullanıcı adı ve parola kısmında eğer kullanıcı adı ve parola aşağıda verilen bilgiler ile
aynı ise "Giriş Başarılı" çıktısı veren, eğer kullanıcı adı doğru şifre yanlış ise "Lütfen Şifrenizi Kontrol Ediniz!" yada
tam tersi kullanıcı adı yanlış ise "Böyle Bir Kullanıcı Bulunamadı!" çıktısı veren programı tasarlayın.

kullanıcı adı: denemekullanici
sifre: 123123123abc
' 
"""



kullanici_adi = input("Lütfen kullanıcı adını giriniz: ")
parola = input("Lütfen şifrenizi giriniz: ")

if kullanici_adi == "denemekullanici" and parola == "123123123abc":
  print("Giriş Başarılı")
elif kullanici_adi != "denemekullanici":
  print("Böyle Bir Kullanıcı Bulunamadı!")
elif parola != "123123123abc":
  print("Lütfen Şifrenizi Kontrol Ediniz!")
